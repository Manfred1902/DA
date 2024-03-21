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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def startTakeoff(self):
        self.app.change_screen("controller_screen")
        #drone.startTest(self.ids["takeoff_height"].text)
        print('Done')

    def startRotate(self):
        self.app.change_screen("controller_screen")
        #drone.rotate(self.ids["rotation_grad"].text, self.ids["rotation_height"].text)

    def startDiagonalFlight(self):
        self.app.change_screen("controller_screen")
        #drone.diagonalFlightTest(self.ids["diagonal_flight_length"].text, self.ids["diagonal_flight_height"].text)

    def startCoordinationFlight(self):
        self.app.change_screen("controller_screen")
        #drone.coordinationFlightTest(self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startFrontFlip(self):
        self.app.change_screen("controller_screen")
        #drone.frontFlip(self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startBackFlip(self):
        self.app.change_screen("controller_screen")
        #drone.backFlip(self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startRightFlip(self):
        self.app.change_screen("controller_screen")
        #drone.rightFlip(self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

    def startLeftFlip(self):
        self.app.change_screen("controller_screen")
        #drone.leftFlip(self.ids["coordination_cord_xyx"].text, self.ids["coordination_height"].text)

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

    def forward(self, instance):
        print("Finished")

    def backward(self, instance):
        pass

    def up(self, instance):
        pass

    def down(self, instance):
        pass

    def left(self, instance):
        pass

    def right(self, instance):
        pass

    def rotateLeft(self, instance):
        pass

    def rotateRight(self, instance):
        pass

    def connect(self, instance):
        video = TelloImageApp(); 
        video.build()

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
