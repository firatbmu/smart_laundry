from threading import Thread

from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar

from services.api import join_queue, get_machine_queue, leave_queue


class QueueScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="queue", **kwargs)
        self._machine = None
        self._my_queue_entry = None
        self._dialog = None
        self._build_ui()

    def _build_ui(self):
        root = MDBoxLayout(orientation="vertical")

        self.toolbar = MDTopAppBar(
            title="Sıraya Gir",
            left_action_items=[["arrow-left", lambda x: self._go_back()]],
            md_bg_color=(0.129, 0.588, 0.953, 1),
        )
        root.add_widget(self.toolbar)

        content = MDBoxLayout(
            orientation="vertical",
            padding=[dp(16), dp(20)],
            spacing=dp(16),
        )

        # Makine bilgi kartı
        self.machine_card = MDCard(
            orientation="vertical",
            padding=dp(16),
            radius=[dp(10)],
            elevation=2,
            size_hint_y=None,
            height=dp(90),
            md_bg_color=(0.95, 0.97, 1, 1),
        )
        self.machine_name_label = MDLabel(
            text="Makine seçilmedi",
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height=dp(36),
        )
        self.machine_status_label = MDLabel(
            text="",
            font_style="Caption",
            theme_text_color="Hint",
            size_hint_y=None,
            height=dp(24),
        )
        self.machine_card.add_widget(self.machine_name_label)
        self.machine_card.add_widget(self.machine_status_label)
        content.add_widget(self.machine_card)

        # Öğrenci numarası alanı
        self.student_input = MDTextField(
            hint_text="Öğrenci numaranız",
            helper_text="Örn: 2021123456",
            helper_text_mode="on_focus",
            icon_right="account",
            size_hint_y=None,
            height=dp(56),
        )
        content.add_widget(self.student_input)

        # Sıraya gir butonu
        self.join_btn = MDRaisedButton(
            text="SIRAYA GİR",
            md_bg_color=(0.129, 0.588, 0.953, 1),
            size_hint_x=1,
            height=dp(48),
            on_release=self._on_join,
        )
        content.add_widget(self.join_btn)

        # Mevcut sıra durumu kartı (başlangıçta gizli)
        self.queue_status_card = MDCard(
            orientation="vertical",
            padding=dp(16),
            radius=[dp(10)],
            elevation=2,
            size_hint_y=None,
            height=dp(120),
            md_bg_color=(0.878, 0.965, 0.878, 1),
            opacity=0,
        )
        self.queue_pos_label = MDLabel(
            text="",
            font_style="H5",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=dp(44),
        )
        self.queue_info_label = MDLabel(
            text="",
            font_style="Body2",
            halign="center",
            size_hint_y=None,
            height=dp(28),
        )
        self.cancel_btn = MDFlatButton(
            text="SIRAYI İPTAL ET",
            theme_text_color="Custom",
            text_color=(0.8, 0.1, 0.1, 1),
            on_release=self._on_cancel,
        )
        cancel_row = MDBoxLayout(size_hint_y=None, height=dp(36))
        cancel_row.add_widget(MDLabel())
        cancel_row.add_widget(self.cancel_btn)
        cancel_row.add_widget(MDLabel())
        self.queue_status_card.add_widget(self.queue_pos_label)
        self.queue_status_card.add_widget(self.queue_info_label)
        self.queue_status_card.add_widget(cancel_row)
        content.add_widget(self.queue_status_card)

        root.add_widget(content)
        self.add_widget(root)

    def set_machine(self, machine_data):
        self._machine = machine_data
        from components.machine_card import STATUS_LABELS
        self.machine_name_label.text = machine_data.get("name", "Makine")
        status = machine_data.get("status", "")
        self.machine_status_label.text = f"Durum: {STATUS_LABELS.get(status, status)}"
        self.toolbar.title = f"Sıra — {machine_data.get('name', '')}"
        self._my_queue_entry = None
        self.queue_status_card.opacity = 0
        self.join_btn.disabled = False
        self.student_input.text = ""

    def _on_join(self, *args):
        student_id = self.student_input.text.strip()
        if not student_id:
            Snackbar(text="Lütfen öğrenci numaranızı girin.").open()
            return
        if not self._machine:
            return
        self.join_btn.disabled = True
        Thread(
            target=self._do_join,
            args=(self._machine["id"], student_id),
            daemon=True,
        ).start()

    def _do_join(self, machine_id, student_id):
        result, error = join_queue(machine_id, student_id)
        Clock.schedule_once(lambda dt: self._on_join_result(result, error, student_id))

    def _on_join_result(self, result, error, student_id):
        if error:
            Snackbar(text=f"Hata: {error}").open()
            self.join_btn.disabled = False
        else:
            self._my_queue_entry = result
            position = result.get("position", "?")
            self.queue_pos_label.text = f"Sıra numaranız: {position}"
            self.queue_info_label.text = f"Öğrenci: {student_id}"
            self.queue_status_card.opacity = 1
            self.join_btn.disabled = True
            Snackbar(text="Sıraya başarıyla girdiniz!").open()

    def _on_cancel(self, *args):
        if not self._my_queue_entry:
            return
        self._dialog = MDDialog(
            title="Sırayı İptal Et",
            text="Sıradan çıkmak istediğinize emin misiniz?",
            buttons=[
                MDFlatButton(text="VAZGEÇ", on_release=lambda x: self._dialog.dismiss()),
                MDRaisedButton(
                    text="İPTAL ET",
                    md_bg_color=(0.8, 0.1, 0.1, 1),
                    on_release=self._do_cancel,
                ),
            ],
        )
        self._dialog.open()

    def _do_cancel(self, *args):
        self._dialog.dismiss()
        entry = self._my_queue_entry
        Thread(
            target=self._cancel_request,
            args=(entry["id"], entry["student_id"]),
            daemon=True,
        ).start()

    def _cancel_request(self, queue_id, student_id):
        success, error = leave_queue(queue_id, student_id)
        Clock.schedule_once(lambda dt: self._on_cancel_result(success, error))

    def _on_cancel_result(self, success, error):
        if success:
            self._my_queue_entry = None
            self.queue_status_card.opacity = 0
            self.join_btn.disabled = False
            Snackbar(text="Sıra iptal edildi.").open()
        else:
            Snackbar(text=f"İptal başarısız: {error}").open()

    def _go_back(self):
        self.manager.current = "machine_list"
