import random
import string
from datetime import datetime

import cv2
import numpy as np
from djitellopy import Tello
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger
from kivymd.app import MDApp


class TelloApp:
    def __init__(self, fb):
        self.tello = Tello()
        self.firebase = fb
        self.clock_event = None
        self.record = False
        self.video = None
        self.video_stream_active: bool = False
        Logger.info('TelloApp: Initialized')

    def toggle_video(self) -> None:
        try:
            if self.video_stream_active:
                self.tello.streamoff()
                MDApp.get_running_app().root.ids["controller_screen"].ids["toggle_videostream"].text = 'Start Videostream'
                if self.clock_event is not None:
                    self.clock_event.cancel()

                self.video_stream_active = False
            else:
                self.tello.connect()
                self.tello.streamon()
                self.video_stream_active = True

                MDApp.get_running_app().root.ids["controller_screen"].ids["toggle_videostream"].text = 'Close Videostream'
                self.clock_event = Clock.schedule_interval(self.update, 1.0 / 30.0)

        except (Exception,) as e:
            Logger.error(e)

    def update(self, dt):
        try:
            frame = self.tello.get_frame_read().frame

            if frame is not None:
                texture = self.convert_frame_to_texture(frame)
                MDApp.get_running_app().root.ids["controller_screen"].ids["video_stream"].texture = texture

                if self.record:
                    texture_data = self.texture_to_np(texture)
                    self.video.write(texture_data)

        except (Exception,) as e:
            Logger.error(e)

    @staticmethod
    def convert_frame_to_texture(frame):
        try:
            h, w, _ = frame.shape

            image = cv2.resize(frame, (w, h))
            buffer = cv2.flip(image, 0).tobytes()

            texture = Texture.create(size=(w, h), colorfmt='rgb')
            texture.blit_buffer(buffer, colorfmt='rgb', bufferfmt='ubyte')

            return texture
        except (Exception,) as e:
            Logger.error(e)

    def save_drone_data(self) -> None:
        try:
            battery: int = self.tello.get_battery()  # Current battery percentage: 0-100
            flight_time: int = self.tello.get_flight_time()  # flight time of the motors in seconds
            avg_temp: float = self.tello.get_temperature()  # average temp in °C
            barometer: int = self.tello.get_barometer()  # absolute height in cm

            self.firebase.send_data(battery, flight_time, avg_temp, barometer)

        except (Exception,) as e:
            Logger.error(e)

    def save_image(self) -> None:
        try:
            # get the current texture
            texture = MDApp.get_running_app().root.ids["controller_screen"].ids["video_stream"].texture

            if texture:
                texture_data = self.texture_to_np(texture)

                # Generate random filename
                filename = self.generate_random_filename('.jpg')

                # save the image
                cv2.imwrite(filename, texture_data)

                # here should be the database method
                self.firebase.save_picture(filename)

        except (Exception,) as e:
            Logger.error(e)

    def record_video(self) -> None:
        try:
            if self.record:
                self.video.release()
                self.record = False
                self.video = None
                MDApp.get_running_app().root.ids["controller_screen"].ids["record_video"].text = "Record Video"
            else:
                texture = MDApp.get_running_app().root.ids["controller_screen"].ids["video_stream"].texture

                if texture:
                    self.record = True
                    MDApp.get_running_app().root.ids["controller_screen"].ids["record_video"].text = "Stop Video Recording"
                    size = texture.size
                    codec = cv2.VideoWriter.fourcc(*'MJPG')  # XVID
                    self.video = cv2.VideoWriter(self.generate_random_filename('.avi'), codec, 30, (size[1], size[0]))

        except (Exception,) as e:
            Logger.error(e)

    @staticmethod
    def texture_to_np(texture):
        # convert Kivy texture to a numpy array
        buffer = texture.pixels
        size = texture.size
        fmt = texture.colorfmt
        texture_data = np.frombuffer(buffer, dtype='uint8').reshape(size[1], size[0], 4)

        # convert RGBA to RGB if necessary
        if fmt == 'rgba':
            texture_data = texture_data[..., :3]

        # rotate 180 degrees
        rotated_texture_data = cv2.rotate(texture_data, cv2.ROTATE_180)

        # flip image
        flipped_texture_data = cv2.flip(rotated_texture_data, 1)

        return flipped_texture_data

    @staticmethod
    def generate_random_filename(extension: str) -> str:
        random_length = random.randint(3, 6)
        random_letters = ''.join(random.choices(string.ascii_letters, k=random_length))
        return random_letters + '_' + str(datetime.now().timestamp()) + extension
