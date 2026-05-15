from threading import Thread

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar

from services.api import register_user


class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="register", **kwargs)
        self._build_ui()

    def _build_ui(self):
        root = MDBoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(
            title="Register",
            left_action_items=[["arrow-left", lambda x: self._go_to("login")]],
            md_bg_color=(0.129, 0.588, 0.953, 1),
        )
        root.add_widget(toolbar)

        scroll = ScrollView()
        body = MDBoxLayout(
            orientation="vertical",
            padding=[dp(32), dp(24)],
            spacing=dp(12),
            size_hint_y=None,
        )
        body.bind(minimum_height=body.setter("height"))

        body.add_widget(MDLabel(
            text="Create New Account",
            font_style="H6",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=dp(40),
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

        self.ad_input = MDTextField(
            hint_text="First Name",
            icon_right="account",
            size_hint_y=None,
            height=dp(56),
        )
        body.add_widget(self.ad_input)

        self.soyad_input = MDTextField(
            hint_text="Last Name",
            icon_right="account",
            size_hint_y=None,
            height=dp(56),
        )
        body.add_widget(self.soyad_input)

        self.telefon_input = MDTextField(
            hint_text="Phone Number",
            helper_text="e.g. 05XX XXX XX XX",
            helper_text_mode="on_focus",
            icon_right="phone",
            input_filter="int",
            size_hint_y=None,
            height=dp(56),
        )
        body.add_widget(self.telefon_input)

        self.sifre_input = MDTextField(
            hint_text="Password",
            helper_text="At least 6 characters",
            helper_text_mode="on_focus",
            password=True,
            icon_right="eye-off",
            size_hint_y=None,
            height=dp(56),
        )
        body.add_widget(self.sifre_input)

        self.register_btn = MDRaisedButton(
            text="REGISTER",
            md_bg_color=(0.129, 0.588, 0.953, 1),
            size_hint_x=1,
            height=dp(52),
            on_release=self._on_register,
        )
        body.add_widget(self.register_btn)

        login_row = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(40),
            spacing=dp(4),
        )
        login_row.add_widget(MDLabel(
            text="Already have an account?",
            halign="right",
            theme_text_color="Hint",
        ))
        login_btn = MDFlatButton(
            text="SIGN IN",
            theme_text_color="Custom",
            text_color=(0.129, 0.588, 0.953, 1),
            on_release=lambda x: self._go_to("login"),
        )
        login_row.add_widget(login_btn)
        body.add_widget(login_row)

        scroll.add_widget(body)
        root.add_widget(scroll)
        self.add_widget(root)

    def on_enter(self):
        for field in (self.tc_input, self.ad_input, self.soyad_input,
                      self.telefon_input, self.sifre_input):
            field.text = ""
        self.register_btn.disabled = False

    def _on_register(self, *args):
        tc = self.tc_input.text.strip()
        ad = self.ad_input.text.strip()
        soyad = self.soyad_input.text.strip()
        telefon = self.telefon_input.text.strip()
        sifre = self.sifre_input.text

        if len(tc) != 11 or not tc.isdigit():
            self._snackbar("National ID must be 11 digits.")
            return
        if not ad:
            self._snackbar("First name cannot be empty.")
            return
        if not soyad:
            self._snackbar("Last name cannot be empty.")
            return
        if not telefon:
            self._snackbar("Phone number cannot be empty.")
            return
        if len(sifre) < 6:
            self._snackbar("Password must be at least 6 characters.")
            return

        self.register_btn.disabled = True
        Thread(
            target=self._do_register,
            args=(tc, ad, soyad, telefon, sifre),
            daemon=True,
        ).start()

    def _do_register(self, tc, ad, soyad, telefon, sifre):
        user, error = register_user(tc, ad, soyad, telefon, sifre)
        Clock.schedule_once(lambda dt: self._on_result(user, error))

    def _snackbar(self, text):
        toast(text)

    def _on_result(self, user, error):
        if error:
            self._snackbar(f"Error: {error}")
            self.register_btn.disabled = False
        else:
            self._snackbar("Registration successful! You can now sign in.")
            Clock.schedule_once(lambda dt: self._go_to("login"), 1.5)

    def _go_to(self, screen_name):
        self.manager.current = screen_name
