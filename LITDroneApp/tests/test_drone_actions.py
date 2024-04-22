from ..core import drone_controller
from core import drone_controller

while True:
    eingabe = input("Gib deine Bewegung ein('stop' für exit): ")
    if eingabe.lower() != "stop":
        drone_controller.manuellTakeover(eingabe.lower)
    else:
        break

