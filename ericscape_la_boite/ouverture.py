# Imports go at the top
from microbit import *
import radio


def ouverture():
    """réveil du servo moteur en analogique. 
    20ms est déjà la valeur de période par défaut mais précisé par précaution"""
    pin0.set_analog_period(20)
    pin0.write_analog(70)#70 : ouvert
    sleep(1000)
    pin0.write_analog(50)#50 : fermé
    sleep(1000)
    
# Servo control: 
# 50 = ~1 millisecond pulse all right 
# 75 = ~1.5 millisecond pulse center 
# 100 = ~2.0 millisecond pulse all left 

radio.config(group=23)
radio.on()

while True:
    """En mode analogique, on a des pulsations régulièrement (toutes les 20 ms)
    ce qui peut dépenser de l'énergie inutilement dans le cadre de ce programme.
    Deux solutions pour économiser dans les moments où on n'utilise pas le servo moteur:
    - changer la période de pulsations
    - passer en digital
    On constate bien la différence: le servo moteur n'exercice pas de résistance si on essaye de le pousser"""
    #pin0.set_analog_period(1000)
    pin0.write_digital(0)
    if button_a.was_pressed() :
        ouverture()

    message = radio.receive()
    if message == 'ok':
        ouverture()