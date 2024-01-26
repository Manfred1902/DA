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

class HomeScreen(MDScreen):
    def conntect_to_drone(self, instance):
        drone.connection()
        print("Finished")
    
    def takeoff(self, instance):
        drone.startTest()
        print("Finished")

    def rotate(self, instance):
        drone.rotationTest()
        print("Finished")

    def take_picture(self, instance):
        drone.take_picture()
        print("Finished")
    
    def diagonal_flight_test_btn(self, instance):
        drone.diagonalFlightTest()
        print("Finished")

    def coordination_flight_test(self, instance):
        drone.coordinationFlightTest()
        print("Finished")

    def front_flip(self, instance):
        drone.frontFlip()
        print("Finished")

    def right_flip(self, instance):
        drone.rightFlip()
        print("Finished")

    def left_flip(self, instance):
        drone.leftFlip()
        print("Finished")
    
    
    def start1(self, text_input1):
        print("Start1 button pressed with text:", text_input1)
 
    def start2(self, text_input2):
        print("Start2 button pressed with text:", text_input2)

class ControllerScreen(MDScreen):
    pos_hint_top = NumericProperty(0.5)
    pos_hint_right = NumericProperty(0.5)
    def build(self):
        joystick = Joystick(pad_size=0.1, outer_size=0.1, inner_size=0.1, pos_hint={"top":0.8, "right":0.8})
        self.root.add_widget(joystick)
        joystick.bind(pad=self.update_coordinates)

    def update_coordinates(self, joystick, pad):
        x_float = float(str(pad[0])[0:5])
        y_float  =float(str(pad[1])[0:5])
        new_pos_hint_top = self.pos_hint_top + y_float
        new_pos_hint_right = self.pos_hint_right + x_float
        # hier könnte man jetzt noch out of bounce prüfen

        # Img nicht mit implementiert
        self.image.pos_hint = {"top":self.pos_hint_top, "right":self.pos_hint_right}

        print("Update fired")

    #def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        #self.add_widget(UpBtn(text='Active Up Button', on_press=self.on_up_btn_press))
        #self.add_widget(DownBtn(text='Active Down Button', on_press=self.on_down_btn_press))

    #def on_up_btn_press(self, instance):
    #    print("Up is being pressed")

    #def on_down_btn_press(self, instance):
    #    print("Down is being pressed")

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
