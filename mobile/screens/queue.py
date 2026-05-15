from threading import Thread

from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.toolbar import MDTopAppBar

from services.api import join_queue, leave_queue, get_my_queue_entry

REFRESH_INTERVAL = 5  # saniye


class QueueScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="queue", **kwargs)
        self._machine = None
        self._my_queue_entry = None
        self._dialog = None
        self._refresh_event = None
        self._build_ui()

    def _build_ui(self):
        root = MDBoxLayout(orientation="vertical")

        self.toolbar = MDTopAppBar(
            title="Join Queue",
            left_action_items=[["arrow-left", lambda x: self._go_back()]],
            right_action_items=[["refresh", lambda x: self._manual_refresh()]],
            md_bg_color=(0.129, 0.588, 0.953, 1),
        )
        root.add_widget(self.toolbar)

        content = MDBoxLayout(
            orientation="vertical",
            padding=[dp(16), dp(20)],
            spacing=dp(16),
        )

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
            text="No machine selected",
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

        self.user_info_card = MDCard(
            orientation="vertical",
            padding=dp(12),
            radius=[dp(10)],
            elevation=1,
            size_hint_y=None,
            height=dp(60),
            md_bg_color=(0.97, 0.97, 0.97, 1),
        )
        self.user_label = MDLabel(
            text="",
            font_style="Body2",
            size_hint_y=None,
            height=dp(24),
        )
        self.tc_label = MDLabel(
            text="",
            font_style="Caption",
            theme_text_color="Hint",
            size_hint_y=None,
            height=dp(20),
        )
        self.user_info_card.add_widget(self.user_label)
        self.user_info_card.add_widget(self.tc_label)
        content.add_widget(self.user_info_card)

        self.join_btn = MDRaisedButton(
            text="JOIN QUEUE",
            md_bg_color=(0.129, 0.588, 0.953, 1),
            size_hint_x=1,
            height=dp(52),
            on_release=self._on_join,
        )
        content.add_widget(self.join_btn)

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
            text="CANCEL QUEUE",
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
        self.machine_name_label.text = machine_data.get("name", "Machine")
        status = machine_data.get("status", "")
        self.machine_status_label.text = f"Status: {STATUS_LABELS.get(status, status)}"
        self.toolbar.title = f"Queue — {machine_data.get('name', '')}"
        self._my_queue_entry = None
        self.queue_status_card.opacity = 0
        self.join_btn.disabled = False

        app = MDApp.get_running_app()
        user = getattr(app, "current_user", None)
        if user:
            self.user_label.text = f"{user.get('ad', '')} {user.get('soyad', '')}"
            self.tc_label.text = f"TC: {user.get('tc', '')}"

    def on_enter(self):
        """Ekrana her girildiğinde mevcut sıra kaydını kontrol et ve refresh başlat."""
        self._check_existing_entry()
        self._start_refresh()

    def on_leave(self):
        """Ekrandan çıkınca refresh durdur."""
        self._stop_refresh()

    def _check_existing_entry(self):
        """Kullanıcının bu makine için zaten sırada olup olmadığını kontrol et."""
        app = MDApp.get_running_app()
        user = getattr(app, "current_user", None)
        if not user or not self._machine:
            return
        Thread(
            target=self._fetch_existing,
            args=(self._machine["id"], user["tc"]),
            daemon=True,
        ).start()

    def _fetch_existing(self, machine_id, tc):
        result, error = get_my_queue_entry(machine_id, tc)
        Clock.schedule_once(lambda dt: self._on_existing_result(result, error))

    def _on_existing_result(self, result, error):
        if error or not result:
            return
        entry = result.get("entry")
        position = result.get("position")
        if entry and position is not None:
            self._my_queue_entry = entry
            app = MDApp.get_running_app()
            user = getattr(app, "current_user", {})
            self.queue_pos_label.text = f"Your position: {position}"
            self.queue_info_label.text = f"{user.get('ad', '')} {user.get('soyad', '')}"
            self.queue_status_card.opacity = 1
            self.join_btn.disabled = True

    def _start_refresh(self):
        self._stop_refresh()
        self._refresh_event = Clock.schedule_interval(
            lambda dt: self._refresh_position(), REFRESH_INTERVAL
        )

    def _stop_refresh(self):
        if self._refresh_event:
            self._refresh_event.cancel()
            self._refresh_event = None

    def _refresh_position(self):
        """Sıra pozisyonunu sessizce güncelle (sadece sıradaysa)."""
        if not self._my_queue_entry or not self._machine:
            return
        app = MDApp.get_running_app()
        user = getattr(app, "current_user", None)
        if not user:
            return
        Thread(
            target=self._fetch_refresh,
            args=(self._machine["id"], user["tc"]),
            daemon=True,
        ).start()

    def _fetch_refresh(self, machine_id, tc):
        result, error = get_my_queue_entry(machine_id, tc)
        Clock.schedule_once(lambda dt: self._on_refresh_result(result, error))

    def _on_refresh_result(self, result, error):
        if error or not result:
            return
        entry = result.get("entry")
        position = result.get("position")
        if entry and position is not None:
            self._my_queue_entry = entry
            self.queue_pos_label.text = f"Your position: {position}"
        elif not entry and self._my_queue_entry:
            # Sıra tamamlandı veya iptal edildi
            self._my_queue_entry = None
            self.queue_status_card.opacity = 0
            self.join_btn.disabled = False

    def _manual_refresh(self):
        """Yenile butonuna basılınca makine durumu + sıra pozisyonu güncelle."""
        if not self._machine:
            return
        app = MDApp.get_running_app()
        user = getattr(app, "current_user", None)
        if not user:
            return
        Thread(
            target=self._fetch_refresh_full,
            args=(self._machine["id"], user["tc"]),
            daemon=True,
        ).start()

    def _fetch_refresh_full(self, machine_id, tc):
        from services.api import get_machine, get_my_queue_entry
        machine = get_machine(machine_id)
        entry_data, _ = get_my_queue_entry(machine_id, tc)
        Clock.schedule_once(lambda dt: self._on_full_refresh(machine, entry_data))

    def _on_full_refresh(self, machine, entry_data):
        from components.machine_card import STATUS_LABELS
        if machine:
            status = machine.get("status", "")
            self.machine_status_label.text = f"Status: {STATUS_LABELS.get(status, status)}"
            self._machine = machine
        if entry_data:
            entry = entry_data.get("entry")
            position = entry_data.get("position")
            if entry and position is not None:
                self._my_queue_entry = entry
                self.queue_pos_label.text = f"Your position: {position}"
                self.queue_status_card.opacity = 1
                self.join_btn.disabled = True
            elif not entry:
                self._my_queue_entry = None
                self.queue_status_card.opacity = 0
                self.join_btn.disabled = False

    def _snackbar(self, text):
        toast(text)

    def _on_join(self, *args):
        app = MDApp.get_running_app()
        user = getattr(app, "current_user", None)
        if not user:
            self._snackbar("Please sign in first.")
            return
        if not self._machine:
            return

        self.join_btn.disabled = True
        Thread(
            target=self._do_join,
            args=(self._machine["id"], user["tc"]),
            daemon=True,
        ).start()

    def _do_join(self, machine_id, tc):
        result, error = join_queue(machine_id, tc)
        Clock.schedule_once(lambda dt: self._on_join_result(result, error))

    def _on_join_result(self, result, error):
        if error:
            self._snackbar(f"Error: {error}")
            self.join_btn.disabled = False
        else:
            self._my_queue_entry = result
            position = result.get("position", "?")
            self.queue_pos_label.text = f"Your position: {position}"
            app = MDApp.get_running_app()
            user = getattr(app, "current_user", {})
            self.queue_info_label.text = f"{user.get('ad', '')} {user.get('soyad', '')}"
            self.queue_status_card.opacity = 1
            self.join_btn.disabled = True
            self._snackbar("Successfully joined the queue!")

    def _on_cancel(self, *args):
        if not self._my_queue_entry:
            return
        self._dialog = MDDialog(
            title="Cancel Queue",
            text="Are you sure you want to leave the queue?",
            buttons=[
                MDFlatButton(text="NO", on_release=lambda x: self._dialog.dismiss()),
                MDRaisedButton(
                    text="YES, CANCEL",
                    md_bg_color=(0.8, 0.1, 0.1, 1),
                    on_release=self._do_cancel,
                ),
            ],
        )
        self._dialog.open()

    def _do_cancel(self, *args):
        self._dialog.dismiss()
        entry = self._my_queue_entry
        app = MDApp.get_running_app()
        user = getattr(app, "current_user", {})
        Thread(
            target=self._cancel_request,
            args=(entry["id"], user.get("tc", "")),
            daemon=True,
        ).start()

    def _cancel_request(self, queue_id, tc):
        success, error = leave_queue(queue_id, tc)
        Clock.schedule_once(lambda dt: self._on_cancel_result(success, error))

    def _on_cancel_result(self, success, error):
        if success:
            self._my_queue_entry = None
            self.queue_status_card.opacity = 0
            self.join_btn.disabled = False
            self._snackbar("Queue cancelled.")
        else:
            self._snackbar(f"Cancel failed: {error}")

    def _go_back(self):
        self._stop_refresh()
        self.manager.current = "machine_list"
