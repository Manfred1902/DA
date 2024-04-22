
from .drone_controller import *

def main():
    drone = drone()
    while True:
        eingabe = input("Gib deine Bewegung ein('stop' für exit): ")
        if eingabe.lower() != "stop":
            drone.manuellTakeover(eingabe.lower)
        else:
            break


