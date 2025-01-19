from microbit import *

while True:
    # Lire la valeur de la broche P0
    signal = pin0.read_analog()
    print(signal)
    
    # Vérifier si le signal est détecté
    if pin0.is_touched():   # seuil à ajuster selon la sensibilité désirée
        display.show(Image.HEART)  # Affiche un cœur si la chaîne est complète
        uart.write("chain_detected\n") # Puis lance un message sur le port serial
    else:
        display.clear()  # Rien si la chaîne est brisée