from microbit import *
import radio

# messages radio enclanchant l'ouverture
MESSAGES = ["boite1", "sem"]

# Configuration des angles
# Selon la documentation :
# 50 = ~1 millisecond pulse all right 
# 75 = ~1.5 millisecond pulse center 
# 100 = ~2.0 millisecond pulse all left 
angle_fermeture = 30 #plusieurs essais, de 50 à 70 pour ouverture
angle_ouverture = 50 #plusieurs essais, de 30 à 50 pour fermeture


def ouverture():
    # affiche un cœur sur l'écran pour indiquer qu'on va ouvrir la boite
    display.show(Image.HEART)
    """réveil du servo moteur en analogique. 
    20ms est déjà la valeur de période par défaut mais précisé par précaution"""
    pin0.set_analog_period(20)
    pin0.write_analog(angle_ouverture)
    sleep(1000)
    pin0.write_analog(angle_fermeture)
    sleep(1000)
    # fin de l'affichage du cœur, pour indiquer la fin de l'ouverture
    display.clear()

    
radio.config(group=23)
radio.on()

pin0.write_analog(angle_fermeture)

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
    if message in MESSAGES:
        ouverture()