from threading import Thread

from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar

from services.api import login_user


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="login", **kwargs)
        self._build_ui()

    def _build_ui(self):
        root = MDBoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="Smart Laundry",
            md_bg_color=(0.129, 0.588, 0.953, 1),
        )
        root.add_widget(toolbar)

        body = MDBoxLayout(
            orientation="vertical",
            padding=[dp(32), dp(40)],
            spacing=dp(16),
        )

        body.add_widget(MDLabel(
            text="Sign In",
            font_style="H5",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=dp(48),
        ))

        self.tc_input = MDTextField(
            hint_text="National ID Number",
            helper_text="Your 11-digit national ID",
            helper_text_mode="on_focus",
            icon_right="card-account-details",
            max_text_length=11,
            input_filter="int",
            size_hint_y=None,
            height=dp(56),
        )
        body.add_widget(self.tc_input)

        self.sifre_input = MDTextField(
            hint_text="Password",
            password=True,
            icon_right="eye-off",
            size_hint_y=None,
            height=dp(56),
        )
        body.add_widget(self.sifre_input)

        self.login_btn = MDRaisedButton(
            text="SIGN IN",
            md_bg_color=(0.129, 0.588, 0.953, 1),
            size_hint_x=1,
            height=dp(52),
            on_release=self._on_login,
        )
        body.add_widget(self.login_btn)

        register_row = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(40),
            spacing=dp(4),
        )
        register_row.add_widget(MDLabel(
            text="Don't have an account?",
            halign="right",
            theme_text_color="Hint",
        ))
        register_btn = MDFlatButton(
            text="REGISTER",
            theme_text_color="Custom",
            text_color=(0.129, 0.588, 0.953, 1),
            on_release=lambda x: self._go_to("register"),
        )
        register_row.add_widget(register_btn)
        body.add_widget(register_row)

        root.add_widget(body)
        self.add_widget(root)

    def on_enter(self):
        self.tc_input.text = ""
        self.sifre_input.text = ""
        self.login_btn.disabled = False

    def _on_login(self, *args):
        tc = self.tc_input.text.strip()
        sifre = self.sifre_input.text

        if len(tc) != 11 or not tc.isdigit():
            self._snackbar("National ID must be 11 digits.")
            return
        if not sifre:
            self._snackbar("Password cannot be empty.")
            return

        self.login_btn.disabled = True
        Thread(target=self._do_login, args=(tc, sifre), daemon=True).start()

    def _do_login(self, tc, sifre):
        user, error = login_user(tc, sifre)
        Clock.schedule_once(lambda dt: self._on_result(user, error))

    def _snackbar(self, text):
        toast(text)

    def _on_result(self, user, error):
        if error:
            self._snackbar(f"Error: {error}")
            self.login_btn.disabled = False
        else:
            app = MDApp.get_running_app()
            app.current_user = user
            self._go_to("machine_list")

    def _go_to(self, screen_name):
        self.manager.current = screen_name
