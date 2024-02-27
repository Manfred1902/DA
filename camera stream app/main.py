from djitellopy import tello
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock

class TelloImageApp(App):
    me = tello.Tello()
    me.connect()
    me.streamoff()
    me.streamon()
    def build(self):
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
        

if __name__ == '__main__':
    TelloImageApp().run()
