from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="home", **kwargs)
        self._build_ui()

    def _build_ui(self):
        root = MDBoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="Akıllı Çamaşırhane",
            md_bg_color=(0.129, 0.588, 0.953, 1),
        )
        root.add_widget(toolbar)

        body = MDBoxLayout(
            orientation="vertical",
            padding=[dp(32), dp(48)],
            spacing=dp(24),
        )

        body.add_widget(MDLabel(
            text="Hoş Geldiniz",
            font_style="H4",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=dp(56),
        ))

        body.add_widget(MDLabel(
            text="Çamaşır makinelerinin durumunu\ngörüntüleyin ve sıraya girin.",
            font_style="Body1",
            halign="center",
            theme_text_color="Hint",
            size_hint_y=None,
            height=dp(60),
        ))

        machines_btn = MDRaisedButton(
            text="MAKİNE DURUMU",
            md_bg_color=(0.129, 0.588, 0.953, 1),
            size_hint_x=1,
            height=dp(52),
            on_release=lambda x: self._go_to("machine_list"),
        )
        body.add_widget(machines_btn)

        root.add_widget(body)
        self.add_widget(root)

    def _go_to(self, screen_name):
        self.manager.current = screen_name
