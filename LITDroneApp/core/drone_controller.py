from .drone_commands import *

def connection():
    try:
        connect_to_drone()
    except:
        print("failed to connect to drone")

def start():
    take_off_land()
    print("flight succsessful")

def rotationTest():
    send_rc_control_async()
    print("flight succsessful")

    