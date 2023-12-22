from djitellopy import Tello
import time

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

print("Takeoff!")
tello.takeoff()

time.sleep(1)

print("Flip left")
tello.flip_forward()

time.sleep(2)

print("Flip Right")
tello.flip_back()

# try flip_forward
# try flip_back
# flip only works with over 50 % energy

print("landing")
tello.land()
print("touchdown.... goodbye")
