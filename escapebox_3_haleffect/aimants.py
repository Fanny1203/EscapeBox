# Imports go at the top
from microbit import *
import radio


radio.config(group=23)




seuils = [100,100,100] # à mettre la médiane...
pins = [pin0, pin1, pin2]
liste = [7,7,7]
listeCorrecte = [1,2,0]
values = [0,0,0]
diffRelatives= [0,0,0]
oldDiffRelatives = [0.0,0.0,0.0]

def getLectureMediane(pin, nbLectures):
    valeurs = []
    for compteur in range(nbLectures):
        valeurs.append(pin.read_analog())
    valeurs.sort()
    mediane = valeurs[nbLectures // 2]
    return mediane


for pin in pins :
    pin.set_pull(pin.PULL_UP)


for i in range(3):
    seuils[i]=getLectureMediane(pins[i],500)
    print(i,") La valeur médiane est "+str(seuils[i]))

# Code in a 'while True:' loop repeats forever
while True:
    for index, pin in enumerate(pins) :
        oldDiffRelatives[index] = diffRelatives[index]
        values[index] = pin.read_analog()
        diffRelatives[index]=abs(values[index]-seuils[index])/seuils[index]
        if (diffRelatives[index]>0.10) and (oldDiffRelatives[index] <0.10): # la pièce 'index' vient d'être mise
            display.show(Image.HAPPY)
            sleep(500)
            display.clear()
            liste.append(index)
            liste.pop(0)
            
    if liste == listeCorrecte :
        print("liste correcte")
        for index,pin in enumerate(pins) :
            if diffRelatives[index] <0.10 : # une pièce n'est pas mise
                print("une pièce a été retirée")
                break
        print("GAGNE")
        display.show(Image.HEART)
        radio.on()
        radio.send('aimants')
        sleep(1000)
        radio.off()
    print("diff relatives :",diffRelatives)
    print("code",str(liste)," - code bon",str(listeCorrecte))
    print("##################################")
    sleep(3000)