from .drone_commands import *

class drone:

    #------------------Basic Tests------------------
    def connection():
        try:
            connect_to_drone()
        except:
            print("failed to connect to drone")

    def startTest():
        try:
            take_off_land()
            print("flight succsessful")
        except:
            print("something went wrong")

    def rotationTest():
        try:
            send_rc_control_async()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def diagonalFlightTest():
        try:
            criss_cross()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def coordinationFlightTest():
        try:
            go_xyz()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def frontFlip():
        try:
            flip_forward()
            print("test succsessful")  
        except:
            print("something went wrong")
        
    def backFlip():
        try:
            flip_backwards()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def rightFlip():
        try:
            flipt_right()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def leftFlip():
        try:
            flip_left()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def leftFlightTest():
        try:
            move_left()
            print("test succsessful")
        except:
            print("something went wrong")
          
    def rightFlightTest():
        try:
            move_right()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def forwardFlightTest():
        try:
            move_forward()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def backwardsFlightTest():
        try:
            move_backwards()
            print("test succsessful")
        except:
            print("something went wrong") 

    def rotaionClockwiseTest():
        try:
            rotate_cw()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def rotationCounterClockwiseTest():
        try:
            rotate_ccw()
            print("test succsessful")
        except:
            print("something went wrong")
        
    #------------------Follow Me------------------