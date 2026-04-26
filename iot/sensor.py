# sensor.py

from machine import I2C
from time import sleep

class ADXL345:
    """
    ADXL345 ivme sensoru icin MicroPython sinifi (class).
    Bu sinif, sensorle ilgili tum islevleri bir araya toplar.
    """

    # Sensorun register adresleri ve temel ayarlari
    _POWER_CTL_REG = 0x2D
    _DATA_FORMAT_REG = 0x31
    _DATA_START_REG = 0x32
    _DEFAULT_ADDR = 0x53

    def __init__(self, i2c, address=_DEFAULT_ADDR):
        """
        Sinif baslatildiginda calisacak ilk metod.
        I2C baglantisini alir ve sensoru olcum icin yapilandirir.
        """
        self.i2c = i2c
        self.address = address
        self._buffer = bytearray(6) # Okuma islemi icin 6 byte'lik bir alan ayiriyoruz.

        # Kalibrasyon icin ofset degerleri
        self.x_offset = 0
        self.y_offset = 0
        self.z_offset = 0

        # Sensoru olcum moduna al
        try:
            self.i2c.writeto_mem(self.address, self._POWER_CTL_REG, b'\x08')
        except OSError as e:
            print(f"Hata: Sensor baslatilamadi. Baglantiyi kontrol edin. {e}")
            raise # Hatayi yukari tasiyarak programin durmasini sagla
        
        # Veri formatini ayarla (varsayilan +/- 2g)
        self.i2c.writeto_mem(self.address, self._DATA_FORMAT_REG, b'\x00')

    def read_raw(self):
        """
        X, Y, Z eksenlerindeki ham (islenmemis) ivme degerlerini okur.
        Donus degeri: (raw_x, raw_y, raw_z) seklinde bir tuple.
        """
        try:
            self.i2c.readfrom_mem_into(self.address, self._DATA_START_REG, self._buffer)
        except OSError as e:
            print(f"Hata: Ham veri okunamadi. {e}")
            return (0, 0, 0)

        # 2 byte'lik veriyi 16-bit isaretli tam sayiya ceviriyoruz
        raw_x = self._buffer[0] | (self._buffer[1] << 8)
        if raw_x > 32767: raw_x -= 65536

        raw_y = self._buffer[2] | (self._buffer[3] << 8)
        if raw_y > 32767: raw_y -= 65536

        raw_z = self._buffer[4] | (self._buffer[5] << 8)
        if raw_z > 32767: raw_z -= 65536
            
        return (raw_x, raw_y, raw_z)

    def read_accel(self):
        """
        X, Y, Z eksenlerindeki ivme degerlerini g (yercekimi) cinsinden okur.
        Donus degeri: (ax, ay, az) seklinde bir tuple.
        """
        raw_x, raw_y, raw_z = self.read_raw()
        
        # Ham degerleri kalibrasyon ofsetleriyle duzeltiyoruz
        raw_x -= self.x_offset
        raw_y -= self.y_offset
        raw_z -= self.z_offset

        # Ham degerleri g'ye cevirmek icin olcekleme faktoru kullaniyoruz
        # Varsayilan +/- 2g hassasiyeti icin bu deger yaklasik 256'dir.
        ax = raw_x / 256.0
        ay = raw_y / 256.0
        az = raw_z / 256.0
        
        return (ax, ay, az)

    def calibrate(self, samples=100):
        """
        Sensoru kalibre etmek icin ofset degerlerini hesaplar.
        Kalibrasyon sirasinda sensorun hareketsiz ve duz bir zeminde olmasi gerekir.
        """
        print("Kalibrasyon basladi. Sensoru 3 saniye boyunca sabit tutun...")
        sleep(3)
        
        sum_x, sum_y, sum_z = 0, 0, 0
        
        print(f"{samples} ornek aliniyor...")
        for _ in range(samples):
            raw_x, raw_y, raw_z = self.read_raw()
            sum_x += raw_x
            sum_y += raw_y
            sum_z += raw_z
            sleep(0.02)

        # Orneklerin ortalamasini alarak ofsetleri buluyoruz
        self.x_offset = sum_x // samples
        self.y_offset = sum_y // samples
        # Z ekseni yercekimini (~1g = +256) hesaptan dusuyoruz
        self.z_offset = (sum_z // samples) - 256 

        print("Kalibrasyon tamamlandi!")
        print(f"Hesaplanan Ofsetler: X={self.x_offset}, Y={self.y_offset}, Z={self.z_offset}")