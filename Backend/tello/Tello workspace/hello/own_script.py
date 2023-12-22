from djitellopy import Tello
import time

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print("Battery Life Percentage: {battery_level}")

print("Takeoff!")
tello.takeoff()

userInput = input()

while(battery_level > 10 and userInput != "stop"):
    if(userInput == "left"):
        print("Move Left")
        tello.move_left(40)
    elif (userInput == "right"):
        print("Move Right")
        tello.move_right(40)
    elif (userInput == "up"):
        print("Move up")
        tello.move_up(40)
    elif (userInput == "down"):
        print("Move down")
        tello.move_down(40)
    elif (userInput == "forward"):
        print("Move forward")
        tello.move_forward(40)
    elif(userInput == "back"):
        print("Move back")
        tello.move_back(40)
    elif(userInput == "rotate right"):
        print("Rotate Clockwise")
        tello.rotate_clockwise(90)
    elif(userInput == "rotate left"):
        print("Rotate Counter Clockwise")
        tello.rotate_counter_clockwise(90)
    elif (userInput == "flip forward"):
        print("Flip forward")
        tello.flip_forward
    elif(userInput == "flip back"):
        print("Flip back")
        tello.flip_back
    elif(userInput == "flip left"):
        print("Flip left")
        tello.flip_left
    elif(userInput == "flip right"):
        print("Flip right")
        tello.flip_right

    print(f"Battery Life Percentage: {battery_level}")
    print("Input: ")
    userInput = input()

print("landing")
tello.land()
print("touchdown.... goodbye")