"""
Les serrures n'étant pas accessibles une fois les boites fermées, vous aurez besoin d'actionner l'ouverture à distance. 
Ce petit code permet d'envoyer un signal radio depuis un deuxième microbit, à l'extérieur.
"""


from microbit import *
import radio

radio.on()
radio.config(group=23)

while True:
    if button_a.was_pressed():
        display.show(Image.HEART)
        radio.send("sem")
        sleep(500)
        display.clear()