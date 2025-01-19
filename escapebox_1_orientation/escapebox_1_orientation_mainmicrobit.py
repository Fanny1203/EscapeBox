from microbit import *

code = '141'
combinaison_correcte = ['n', 'w', 's', 'n','e']
combinaison_joueur = ['-', '-', '-', '-', '-']

# Code in a 'while True:' loop repeats forever
while True:
    if accelerometer.was_gesture('up'):
        display.show(Image.ARROW_S)
        sleep(1000)
        display.clear()
        combinaison_joueur.append('s')
        combinaison_joueur.pop(0)
    elif accelerometer.was_gesture('down'):
        display.show(Image.ARROW_N)
        sleep(1000)
        display.clear()
        combinaison_joueur.append('n')
        combinaison_joueur.pop(0)
    elif accelerometer.was_gesture('left'):
        display.show(Image.ARROW_W)
        sleep(1000)
        display.clear()
        combinaison_joueur.append('w')
        combinaison_joueur.pop(0)
    elif accelerometer.was_gesture('right'):
        display.show(Image.ARROW_E)
        sleep(1000)
        display.clear()
        combinaison_joueur.append('e')
        combinaison_joueur.pop(0)
        print(combinaison_joueur)

    if combinaison_correcte == combinaison_joueur :
        display.scroll(code)

