from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.app import MDApp

from screens.home import HomeScreen
from screens.machine_list import MachineListScreen
from screens.queue import QueueScreen

Window.size = (360, 640)


class SmartLaundryApp(MDApp):
    def build(self):
        self.title = "Akıllı Çamaşırhane"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(HomeScreen())
        sm.add_widget(MachineListScreen())
        sm.add_widget(QueueScreen())
        return sm


if __name__ == "__main__":
    SmartLaundryApp().run()
