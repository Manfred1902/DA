from ..core import *


def main():
    while True:
        eingabe = input("Gib deine Bewegung ein('stop' für exit): ")
        if eingabe.lower() != "stop":
            manuellTakeover(eingabe.lower)
        else:
            break

