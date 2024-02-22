from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


#from kivy.garden.joystick import Joystick
from kivy.properties import NumericProperty

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


from core.drone_controller import *

class Homescreen(MDScreen):
    pass

class HomeScreenExp(MDScreen):
    def on_start():
        sm = MDScreenManager()
        screen = MDScreen()
        box = MDBoxLayout(orientation="vertical", spacing=10, padding=10)
        toolbar = MDTopAppBar(title="My App")
        panel1 = MDExpansionPanel(
            icon="language-python", 
            panel_cls=MDExpansionPanelOneLine(text="Python"), 
            content=MDLabel(text="This is Python.")
        )
        panel2 = MDExpansionPanel(
            icon="language-java", 
            panel_cls=MDExpansionPanelOneLine(text="Java"), 
            content=MDLabel(text="This is Java.")
        )
        box.add_widget(toolbar)
        box.add_widget(panel1)
        box.add_widget(panel2)
        screen.add_widget(box)
        sm.add_widget(screen)
        return sm

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

#class UpBtn(MDFlatButton):
#    def on_touch_down(self, touch):
#        if self.collide_point(*touch.pos):
#            self.background_color = [1, 0, 0, 1]  # Change the background color to red
#            self.dispatch('on_press')
#            return True
#        return super().on_touch_down(touch)

#    def on_touch_up(self, touch):
#        if self.collide_point(*touch.pos):
#            self.background_color = [1, 1, 1, 1]  # Change the background color back to white
#            self.dispatch('on_release')
#            return True
#        return super().on_touch_up(touch)

#class DownBtn(MDFlatButton):
#    def on_touch_down(self, touch):
#        if self.collide_point(*touch.pos):
#            self.background_color = [1, 0, 0, 1]  # Change the background color to red
#            self.dispatch('on_press')
#        return True

#    def on_touch_up(self, touch):
#        if self.collide_point(*touch.pos):
#            self.background_color = [1, 1, 1, 1]  # Change the background color back to white
#            self.dispatch('on_release')
#        return True


if __name__ == "__main__":
    MainApp().run()
