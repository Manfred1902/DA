'''
from djitellopy import tello
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from ultralytics import YOLO

class TelloImageApp(App):
    # load yolov8 model
    model = YOLO('yolov8n.pt')

    #me = tello.Tello()
    #me.connect()
    #me.streamoff()
    #me.streamon()
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    ret = True

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.image_widget = Image()
        layout.add_widget(self.image_widget)
        Clock.schedule_interval(self.update_image, 1.0 / 30.0)
        return layout

    def update_image(self, dt):
        self.ret, frame = self.cap.read()
        results = self.model.track(frame, persist=True)
        frame_ = results[0].plot()

        # Flip the frame vertically
        frame_ = cv2.flip(frame_, 0)

        texture = Texture.create(size=(frame_.shape[1], frame_.shape[0]), colorfmt='bgr')
        texture.blit_buffer(frame_.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        self.image_widget.texture = texture




if __name__ == '__main__':
    TelloImageApp().run()
    '''

from djitellopy import Tello
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from ultralytics import YOLO

class TelloImageApp(App):
    # load yolov8 model
    model = YOLO('yolov8n.pt')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tello = Tello()

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.image_widget = Image()
        layout.add_widget(self.image_widget)
        Clock.schedule_interval(self.update_image, 1.0 / 30.0)
        return layout

    def update_image(self, dt):
        frame = self.tello.get_frame_read().frame
        results = self.model.track(frame, persist=True)
        frame_ = results[0].plot()

        # Flip the frame vertically
        frame_ = cv2.flip(frame_, 0)

        texture = Texture.create(size=(frame_.shape[1], frame_.shape[0]), colorfmt='bgr')
        texture.blit_buffer(frame_.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        self.image_widget.texture = texture

    def on_start(self):
        self.tello.connect()
        self.tello.streamoff()
        self.tello.streamon()

    def on_stop(self):
        self.tello.streamoff()
        self.tello.end()

if __name__ == '__main__':
    TelloImageApp().run()