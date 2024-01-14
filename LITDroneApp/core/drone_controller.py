from .drone_commands import *

class drone:
    def connection():
        try:
            connect_to_drone()
        except:
            print("failed to connect to drone")

    def startTest():
        take_off_land()
        print("flight succsessful")

    def rotationTest():
        send_rc_control_async()
        print("flight succsessful")
    
    def diagonalFlightTest():
        criss_cross()
        print("flight succsessful")
    
    def coordinationFlightTest():
        go_xyz()
        print("flight succsessful")
    
    def frontFlip():
        flip_forward()

    def backFlip():
        flip_backwards()

    def rightFlip():
        flipt_right()

    def leftFlip():
        flip_left()

    

    