from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


# to switch to different pages
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

# Database and login proof
from backend.database import Firebase

# for create a button with push recogition
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button

from kivy.input.motionevent import MotionEvent


# alles für ExpansionPanel
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine
from kivymd.uix.boxlayout import MDBoxLayout


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expansion_panel = MDExpansionPanel(
            title='Expansion Panel Title',
            icon='language-python',
            content=MDExpansionPanelOneLine(text='Expansion Panel Content'),
            panel_cls=MDExpansionPanelOneLine
        )
        self.add_widget(self.expansion_panel)

class ControllerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(UpBtn(text='Active Up Button', on_press=self.on_up_btn_press))
        self.add_widget(DownBtn(text='Active Down Button', on_press=self.on_down_btn_press))

    def on_up_btn_press(self, instance):
        print("Up is being pressed")

    def on_down_btn_press(self, instance):
        print("Down is being pressed")

class SettingsScreen(MDScreen):
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
    def build(self):
        gui = Builder.load_file("temp_kv_files_storage/main.kv")
        # Window.fullscreen = 'auto'
        # Window.borderless = True
        self.db = Firebase()
        return gui

    def change_screen(self, filename):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = NoTransition()
        screen_manager.current = filename
    
    def initFirebase():
        return Firebase()

class UpBtn(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 0, 0, 1]  # Change the background color to red
            self.dispatch('on_press')
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]  # Change the background color back to white
            self.dispatch('on_release')
            return True
        return super().on_touch_up(touch)

class DownBtn(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 0, 0, 1]  # Change the background color to red
            self.dispatch('on_press')
        return True

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]  # Change the background color back to white
            self.dispatch('on_release')
        return True


if __name__ == "__main__":
    MainApp().run()
