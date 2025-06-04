"""
Un petit code pour contrôler un pin en mode digital depuis le bouton A.
"""

from microbit import *

etat = False

while True:
    if button_a.was_pressed():
        etat = not etat
        if etat:
            pin0.write_digital(1)
            display.show(Image.HEART)
        else:
            pin0.write_digital(0)
            display.clear()