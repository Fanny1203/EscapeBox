from microbit import *
import music
import radio

radio.config(group=23)

# Configuration du servo-moteur
def set_angle(angle):
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    duty = 26 + (angle * 102) // 180
    pin0.write_analog(duty)

COURT = 300  # Durée en ms pour un appui court
LONG = 500   # Durée en ms pour un appui long
PAUSE = 1000  # Temps d'attente maximum entre deux appuis
CODE = "....__"  # Le code à détecter
MESSAGE_RADIO = "bonbon"

code_saisi = ""

#pour ouvrir la boite à bonbons, paramétrages différents selon microbit 1 ou 2. Préférer arduino ?
def ouverture_boiteabonbons():
    """réveil du servo moteur en analogique. 
    20ms est déjà la valeur de période par défaut mais précisé par précaution"""
    display.show(Image.HAPPY)
    music.play(music.POWER_UP)
    pin0.set_analog_period(20)
    pin0.write_analog(70)#70 : ouvert
    sleep(1000)
    pin0.write_analog(50)#50 : fermé
    sleep(1000)
    display.clear()

#ouverture d'une ericbox contenant un microbit à l'écoute radio
def ouverture():
    display.show(Image.HAPPY)
    radio.on()
    radio.send(MESSAGE_RADIO)
    sleep(1000)
    radio.off()
    sleep(1000)
    display.clear()

# Boucle principale
while True:
    temps_actuel = running_time()
    
    # Si le bouton A est pressé
    if button_a.is_pressed():
        debut_appui = temps_actuel
        # Attendre que le bouton soit relâché
        while button_a.is_pressed():
            sleep(50)
        
        duree_appui = running_time() - debut_appui
        
        # Déterminer si c'est un appui court ou long
        if duree_appui < COURT:
            code_saisi += "."
            #afficher un point
            display.show(Image('00000:'
                               '00000:'
                               '00000:'
                               '09900:'
                               '09900'))
            music.pitch(1000, 100)
        else:
            code_saisi += "_"
            #afficher un trait
            display.show(Image('00000:'
                               '00000:'
                               '00000:'
                               '00000:'
                               '99999'))
            music.pitch(500, 300)
        
        sleep(50)
        display.clear()
        
        # Vérifier les derniers caractères après chaque appui
        if len(code_saisi) >= len(CODE):
            derniers_caracteres = code_saisi[-len(CODE):]
            if derniers_caracteres == CODE:
                ouverture()
                code_saisi = ""
                display.clear()
        
    
