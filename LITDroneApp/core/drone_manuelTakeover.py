from djitellopy import Tello
import cv2
import time
from threading import Thread
from core.utils import *

tello = Tello()

class manuellTakeover:
    manuellTakeover: bool

    def stop(self):
        self.manuellTakeover = False
        tello.streamoff
        cv2.destroyWindow('TelloVideo')
        cv2.destroyAllWindows()

    def move_up(self):
        tello.move_up(1)

    def move_down(self):
        tello.move_down(1)

    def move_left(self):
        tello.move_left(1)

    def move_right(self):
        tello.move_right(1)

    def move_forward(self):
        tello.move_forward(1)

    def move_backwards(self):
        tello.move_back(1)

    def move_clockwise(self): 
        tello.rotate_clockwise(1)

    def move_counter_clockwise(self):
        tello.rotate_counter_clockwise(1)

    # Dictionary, das Funktionen den Optionen zuordnet
    option_actions = {
        ' ': move_up,
        'l': move_down,
        'd': move_left,
        'w': move_forward,
        'a': move_right,
        's': move_backwards,
        'q': move_counter_clockwise,
        'e': move_clockwise,
        'z': stop
    }

    async def control_drone(self, movement):
        self.videofeed()
        action = self.option_actions.get(movement)
        if action:
            self.action(self)
        
    
    async def videofeed():
        manuellTakeover = True
        tello.streamon()
        frame_read = tello.get_frame_read()
        while manuellTakeover==True:
            # read a single image from the Tello video feed
            print("Read Tello Image")
            tello_video_image = frame_read.frame

            # use opencv to write image
            if tello_video_image is not None:
                cv2.imshow("TelloVideo", tello_video_image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    

    
    