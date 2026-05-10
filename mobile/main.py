from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.app import MDApp

from screens.home import HomeScreen
from screens.login import LoginScreen
from screens.machine_list import MachineListScreen
from screens.queue import QueueScreen
from screens.register import RegisterScreen

Window.size = (360, 640)


class SmartLaundryApp(MDApp):
    current_user = None  # Giriş yapan kullanıcı bilgisi burada tutulur

    def build(self):
        self.title = "Smart Laundry"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(HomeScreen())
        sm.add_widget(MachineListScreen())
        sm.add_widget(QueueScreen())
        return sm


if __name__ == "__main__":
    SmartLaundryApp().run()
