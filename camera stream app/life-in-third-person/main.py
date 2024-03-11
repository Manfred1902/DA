from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from core.database import Firebase
from core.tello import TelloApp


class HomeScreen(MDScreen):
    pass


class LoginScreen(MDScreen):
    pass


class SignUpScreen(MDScreen):
    pass


class ForgotPasswordScreen(MDScreen):
    pass


class LabelButton(MDTextButton, MDLabel):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Firebase()
        self.tello = TelloApp(self.db)

    def build(self):
        gui = Builder.load_file("kv/main.kv")
        # Window.fullscreen = 'auto'
        # Window.borderless = True

        return gui

    def change_screen(self, filename):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = filename


if __name__ == "__main__":
    MainApp().run()
