import cv2
from djitellopy import Tello
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger
from kivymd.app import MDApp

from core.database import Firebase


class TelloApp:
    def __init__(self):
        self.tello = Tello()
        self.firebase = Firebase()
        self.clock_event = None
        self.video_stream_active: bool = False
        Logger.info('TelloApp: Initialized')

    def toggle_video(self) -> None:
        try:
            if self.video_stream_active:
                self.tello.streamoff()
                MDApp.get_running_app().root.ids["home_screen"].ids["toggle_videostream"].text = 'Start Videostream'
                if self.clock_event is not None:
                    self.clock_event.cancel()

                self.video_stream_active = False
            else:
                self.tello.connect()
                self.tello.streamon()
                self.video_stream_active = True

                MDApp.get_running_app().root.ids["home_screen"].ids["toggle_videostream"].text = 'Close Videostream'
                self.clock_event = Clock.schedule_interval(self.update, 1.0 / 30.0)

        except (Exception,) as e:
            Logger.error(e)

    def update(self, dt):
        try:
            frame = self.tello.get_frame_read().frame

            if frame is not None:
                texture = self.convert_frame_to_texture(frame)
                MDApp.get_running_app().root.ids["home_screen"].ids["video_stream"].texture = texture
        except (Exception,) as e:
            Logger.error(e)

    def convert_frame_to_texture(self, frame):
        try:
            h, w, _ = frame.shape

            image = cv2.resize(frame, (w, h))
            buffer = cv2.flip(image, 0).tobytes()

            texture = Texture.create(size=(w, h), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')

            return texture
        except (Exception,) as e:
            Logger.error(e)

    async def get_drone_data(self):
        try:
            battery = self.tello.get_battery()
            flight_time = self.tello.get_flight_time()
            avg_temp = self.tello.get_temperature()
            barometer = self.tello.get_barometer()

            await self.firebase.send_data(battery, flight_time, avg_temp, barometer)

        except (Exception,) as e:
            Logger.error(e)
