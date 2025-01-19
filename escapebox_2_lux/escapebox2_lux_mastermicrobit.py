from microbit import *
import music
import radio

taux_changement = 0.10

code_bon = [True,True,False]
code_encours = [False,False,False]

radio.config(group=23)

def getLectureMediane(pin, nbLectures):
    valeurs = []
    for compteur in range(nbLectures):
        valeurs.append(pin.read_analog())
    valeurs.sort()
    mediane = valeurs[nbLectures // 2]
    return mediane

pins=[pin0,pin1,pin2]
for pin in pins:
    pin.set_pull(pin.PULL_DOWN)
medianes=[0,0,0]
for i in range(3):
    medianes[i]=getLectureMediane(pins[i],500)
    print(i,") La valeur médiane est "+str(medianes[i]))
    

sleep(1000)
    

while True:
    valeurs=[0,0,0]
    for i in range(3):
        valeurs[i]=pins[i].read_analog()-medianes[i]
    for i in range(3):
        code_encours[i]=(valeurs[i]>medianes[i]*taux_changement)
    
    print("differences",str(valeurs)," - medianes",str(medianes))
    print("code",str(code_encours)," - code bon",str(code_bon))
    print("##################################")
    
    if code_encours==code_bon :
        #music.play(music.BA_DING)  # Mettre ici l'action voulue, pour l'instant, un son
        radio.on()
        radio.send('lux')
        sleep(1000)
        radio.off()
    else:
        music.stop()
    sleep(3000)  # Pause pour éviter de lire trop fréquemment