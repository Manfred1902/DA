from .drone_commands import *
from .drone_followMe import *
from .drone_manuelTakeover import *
from .exceptions import *

class drone:
    isConnectedToDrone: bool

    def __init__(self):
        self.isConnectedToDrone = False

    #------------------Basic Tests------------------
    async def connection(self):
        try:
            await basicTests.connect_to_drone()
            self.isConnectedToDrone = True
        except:
            print("failed to connect to drone")

    def startTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.take_off_land()
            print("flight succsessful")
        except:
            print("something went wrong")

    def moveUp(self, height = 40):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.move_up(height)
            print("flight succsessful")
        except:
            print("something went wrong")

    def rotationTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.send_rc_control_async()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def diagonalFlightTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.criss_cross()
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def coordinationFlightTest(self, x = 30, y = 30, z = 30, cw = 30):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.go_xyz(x,y,z,cw)
            print("flight succsessful")
        except:
            print("something went wrong")
           
    def frontFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.flip_forward()
            print("test succsessful")  
        except:
            print("something went wrong")
        
    def backFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.flip_backwards()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def rightFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.flipt_right()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def leftFlip(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.flip_left()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def leftFlightTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.move_left()
            print("test succsessful")
        except:
            print("something went wrong")
          
    def rightFlightTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.move_right()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def forwardFlightTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.move_forward()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def backwardsFlightTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.move_backwards()
            print("test succsessful")
        except:
            print("something went wrong") 

    def rotaionClockwiseTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.rotate_cw()
            print("test succsessful")
        except:
            print("something went wrong")
        
    def rotationCounterClockwiseTest(self):
        try:
            if self.isConnectedToDrone==False:
                raise NotConnectedToDrone("you are not connected to the drone")
            basicTests.rotate_ccw()
            print("test succsessful")
        except:
            print("something went wrong")
        
    #------------------Follow Me------------------
    