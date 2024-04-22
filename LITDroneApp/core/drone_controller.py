from .drone_commands import *
from .drone_followMe import *
from .drone_manuelTakeover import *
from .drone_wander import *
from .exceptions import *

class drone:
    isConnectedToDrone: bool

    def __init__(self):
        self.isConnectedToDrone = False

    def connection(self):
        try:
            print("Connect to Tello Drone")
            tello.connect()
            self.isConnectedToDrone = True
        except:
            print("failed to connect to drone")

#------------------1st Features: Basic Checks------------------
    def startCheck(self, height = "40"):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.take_off_land(int(height))
            print("flight succsessful")
        except:
            print("something went wrong")

    def moveUp(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.move_up()
            print("flight succsessful")
        except:
            print("something went wrong")

    def rotationCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.send_rc_control_async()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def diagonalFlightCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.criss_cross()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def coordinationFlightCheck(self, x = 30, y = 30, z = 30, cw = 30):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.go_xyz(x,y,z,cw)
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def frontFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.flip_forward()
            print("test succsessful")  
        except:
            print("something went wrong")
        
    def backFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.flip_backwards()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def rightFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.flipt_right()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def leftFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.flip_left()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def leftFlightCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.move_left()
            print("test succsessful")
        except:
            print("something went wrong")
          
    def rightFlightCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.move_right()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def forwardFlightCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.move_forward()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def backwardsFlightCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.move_backwards()
            print("test succsessful")
        except:
            print("something went wrong") 

    def rotaionClockwiseCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.rotate_cw()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def rotationCounterClockwiseCheck(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicChecks.rotate_ccw()
            print("test succsessful")
        except:
            print("something went wrong")
        
    #------------------Follow Me------------------
    #------------------Manuell Takeover-----------
    def manuellTakeover(self, movement):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            manuellTakeover.control_drone()
        except:
            print("something went wrong")
    