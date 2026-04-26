from threading import Thread

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.toolbar import MDTopAppBar

from components.machine_card import MachineCard
from services.api import get_machines


class MachineListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="machine_list", **kwargs)
        self._build_ui()

    def _build_ui(self):
        root = MDBoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="Çamaşır Makineleri",
            left_action_items=[["arrow-left", lambda x: self._go_back()]],
            right_action_items=[["refresh", lambda x: self.load_machines()]],
            md_bg_color=(0.129, 0.588, 0.953, 1),
        )
        root.add_widget(toolbar)

        self.spinner = MDSpinner(
            size_hint=(None, None),
            size=(dp(46), dp(46)),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            active=True,
        )
        self.spinner_box = MDBoxLayout(
            size_hint_y=None,
            height=dp(80),
            pos_hint={"center_x": 0.5},
        )
        self.spinner_box.add_widget(self.spinner)
        root.add_widget(self.spinner_box)

        scroll = ScrollView()
        self.card_list = MDBoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=[dp(12), dp(8)],
            size_hint_y=None,
        )
        self.card_list.bind(minimum_height=self.card_list.setter("height"))
        scroll.add_widget(self.card_list)
        root.add_widget(scroll)

        self.add_widget(root)

    def on_enter(self):
        self.load_machines()

    def load_machines(self):
        self.spinner_box.opacity = 1
        self.card_list.clear_widgets()
        Thread(target=self._fetch, daemon=True).start()

    def _fetch(self):
        machines = get_machines()
        Clock.schedule_once(lambda dt: self._update_ui(machines))

    def _update_ui(self, machines):
        self.spinner_box.opacity = 0
        self.card_list.clear_widgets()

        if not machines:
            self.card_list.add_widget(MDLabel(
                text="Backend'e bağlanılamadı veya makine yok.",
                halign="center",
                theme_text_color="Hint",
                size_hint_y=None,
                height=dp(60),
            ))
            return

        for m in machines:
            card = MachineCard(
                machine_data=m,
                on_queue_press=self._open_queue_screen,
            )
            self.card_list.add_widget(card)

    def _open_queue_screen(self, machine_data):
        screen = self.manager.get_screen("queue")
        screen.set_machine(machine_data)
        self.manager.current = "queue"

    def _go_back(self):
        self.manager.current = "home"
