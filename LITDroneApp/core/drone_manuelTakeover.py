from djitellopy import Tello
import cv2
from core.utils import *

tello = Tello()

class manuellTakeover:
    manuellTakeover: bool

    def takeoff(self):
        tello.takeoff()
        print("Takeoff")

    def land(self):
        tello.land()
        print("Landing")

    def stop(self):
        self.manuellTakeover = False
        tello.streamoff
        cv2.destroyWindow('TelloVideo')
        cv2.destroyAllWindows()

    def move_up():
        tello.move_up(5)
        print("Move Up")

    def move_down():
        tello.move_down(5)
        print("Move Down")
  
    def move_left():
        print("Move Left")
        tello.move_left(5)

    def move_right():
        print("Move Right")
        tello.move_right(5)

    def move_forward():
        print("Move Forward")
        tello.move_forward(5)

    def move_backwards():
        print("Move Backwards")
        tello.move_back(5)

    def rotate_cw():
        print("Rotate Clockwise")
        tello.rotate_clockwise()

    def rotate_ccw():
        print("Rotate Counter Clockwise")
        tello.rotate_counter_clockwise()

    def flip_left():
        print("Flip left")
        tello.flip_left()

    def flipt_right():
        print("Flip Right")
        tello.flip_right()

    def flip_forward():
        print("Flip forward")
        tello.flip_forward()

    def flip_backwards():
        print("Flip backwards")
        tello.flip_back()
    
