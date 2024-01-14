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
        print("test succsessful")

    def backFlip():
        flip_backwards()
        print("test succsessful")

    def rightFlip():
        flipt_right()
        print("test succsessful")

    def leftFlip():
        flip_left()
        print("test succsessful")

    def leftFlightTest():
        move_left()
        print("test succsessful")
    
    def rightFlightTest():
        move_right()
        print("test succsessful")

    def forwardFlightTest():
        move_forward()
        print("test succsessful")

    def backwardsFlightTest():
        move_backwards()
        print("test succsessful")

    def rotaionClockwiseTest():
        rotate_cw()
        print("test succsessful")

    def rotationCounterClockwiseTest():
        rotate_ccw()
        print("test succsessful")




    