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
from core.drone_controller import *
import core.tello

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
from kivymd.uix.button import MDFlatButton

# Video
from djitellopy import tello
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock

class DescriptionScreen(MDScreen):
    pass

class ContentNavigationDrawer(MDBoxLayout):
    pass
class TelloImageApp(App):

    def build(self):
        me = tello.Tello()
        me.connect()
        me.streamoff()
        me.streamon()
        layout = BoxLayout(orientation='vertical')
        self.image_widget = Image()
        layout.add_widget(self.image_widget)
        Clock.schedule_interval(self.update_image, 1.0 / 30.0)
        return layout

    def update_image(self, dt):
        myFrame = self.me.get_frame_read().frame
        image = cv2.resize(myFrame, (360, 240))
        buffer = cv2.flip(image, 0).tobytes()
        texture = Texture.create(size=(image.shape[1], image.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image_widget.texture = texture

class Content(BoxLayout):
    pass

class HomeScreenExp(MDScreen):
    pass

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def conntect_to_drone(self):
        drone.connection(self)
        print("Finished")

    def startTakeoff(self):
        self.app.change_screen("controller_screen")
        drone.connection(self)
        drone.startCheck(self, self.ids["takeoff_height"].text)

    def startRotate(self):
        self.app.change_screen("controller_screen")
        drone.connection(self)
        drone.rotationCheck(self, self.ids["rotation_grad"].text, self.ids["rotation_height"].text)

    def startDiagonalFlight(self):
        self.app.change_screen("controller_screen")
        drone.diagonalFlightCheck(self, self.ids["diagonal_flight_length"].text, self.ids["diagonal_flight_height"].text)

    def startCoordinationFlight(self):
        self.app.change_screen("controller_screen")
        drone.coordinationFlightCheck(self, self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startFrontFlip(self):
        self.app.change_screen("controller_screen")
        drone.frontFlip(self, self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startBackFlip(self):
        self.app.change_screen("controller_screen")
        drone.backFlip(self, self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startRightFlip(self):
        self.app.change_screen("controller_screen")
        drone.rightFlip(self, self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startLeftFlip(self):
        self.app.change_screen("controller_screen")
        drone.leftFlip(self, self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)


class ControllerScreen(MDScreen):
    def start(self, instance):
        drone.takeoff(self)

    def land(self, instance):
        drone.land(self)

    def forward(self, instance):
        drone.forward(self)

    def backward(self, instance):
        drone.backwards(self)

    def up(self, instance):
        drone.moveUp(self)

    def down(self, instance):
        drone.moveDown(self)

    def left(self, instance):
        drone.moveLeft(self)

    def right(self, instance):
        drone.moveRight(self)

    def rotateLeft(self, instance):
        drone.rotateLeft(self)

    def rotateRight(self, instance):
        drone.rotateRight(self)

    def connect(self, instance):
        drone.connection(self)

    def quit(self):
        if(self.app.isClickable == True):
            self.app.change_screen("home_screen")
        else:
            print("Not allowed")




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
        gui = Builder.load_file("kv_files/main.kv")
        # Window.fullscreen = 'auto'
        # Window.borderless = True
        self.db = Firebase()
        self.tello = core.tello.TelloApp(self.db)
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
