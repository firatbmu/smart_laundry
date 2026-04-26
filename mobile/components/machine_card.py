from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.metrics import dp

STATUS_COLORS = {
    "AVAILABLE": (0.298, 0.686, 0.314, 1),   # Yeşil
    "RUNNING":   (1.0,   0.596, 0.0,   1),   # Turuncu
    "FINISHING": (0.129, 0.588, 0.953, 1),   # Mavi
    "FINISHED":  (0.62,  0.62,  0.62,  1),   # Gri
}

STATUS_LABELS = {
    "AVAILABLE": "Müsait",
    "RUNNING":   "Çalışıyor",
    "FINISHING": "Bitiyor",
    "FINISHED":  "Bitti",
}


class MachineCard(MDCard):
    def __init__(self, machine_data, on_queue_press=None, **kwargs):
        super().__init__(**kwargs)
        self.machine_data = machine_data
        self.on_queue_press = on_queue_press

        self.orientation = "horizontal"
        self.padding = dp(12)
        self.spacing = dp(8)
        self.size_hint_y = None
        self.height = dp(80)
        self.radius = [dp(10)]
        self.elevation = 2
        self.md_bg_color = (1, 1, 1, 1)

        self._build()

    def _build(self):
        status = self.machine_data.get("status", "AVAILABLE")
        color = STATUS_COLORS.get(status, STATUS_COLORS["AVAILABLE"])
        label = STATUS_LABELS.get(status, status)

        # Sol ikon
        icon_btn = MDIconButton(
            icon="washing-machine",
            theme_icon_color="Custom",
            icon_color=color,
            pos_hint={"center_y": 0.5},
        )
        self.add_widget(icon_btn)

        # Orta: isim + durum
        info_box = MDBoxLayout(orientation="vertical", spacing=dp(2))
        info_box.add_widget(MDLabel(
            text=self.machine_data.get("name", "Makine"),
            font_style="Subtitle1",
            bold=True,
            size_hint_y=None,
            height=dp(28),
        ))
        info_box.add_widget(MDLabel(
            text=label,
            theme_text_color="Custom",
            text_color=color,
            font_style="Caption",
            size_hint_y=None,
            height=dp(20),
        ))
        self.add_widget(info_box)

        # Sağ: sıraya gir butonu (sadece RUNNING veya FINISHING durumunda)
        if status in ("RUNNING", "FINISHING") and self.on_queue_press:
            queue_btn = MDIconButton(
                icon="account-clock",
                theme_icon_color="Custom",
                icon_color=(0.129, 0.588, 0.953, 1),
                pos_hint={"center_y": 0.5},
                on_release=lambda x: self.on_queue_press(self.machine_data),
            )
            self.add_widget(queue_btn)
