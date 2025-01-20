# Escape Box - Enigme IA-guirlande

[![Miniature vidéo](https://img.youtube.com/vi/AJQ-Y7U1JHs/0.jpg)](https://www.youtube.com/watch?v=AJQ-Y7U1JHs)


## Description
Sur un ordinateur, une page Internet est affichée avec une camera filme. 
Si la bonne image est montrée à la camérapendant quelques secondes, le javascript envoie un message "IA" en série sur le microbit branché sur l'ordinateur. Ce microbit envoie alors un signal "IA" sur le microbit de la guirlande, en radio. Lun microbit branché sur l'ordinateur envoie un signal "IA".
Un autre microbit déclanche la guirlande lorsqu'il recoit le signal "IA".


## Matériel nécessaire
* Un ordinateur avec un premier microbit branché (communication série entre l'ordinateur et le microbit)
* Sur l'ordinateur, la page web qui filme et fait analyser l'image par le modèle
* Un deuxième microbit branché à la guirlande (voir schéma de montage)


## Partie javascript
* On commence par entrainer un modèle à reconnaitre une image avec teachable machine : https://teachablemachine.withgoogle.com/train (en réalité, on ne fait que ré-entraîner la dernière couche du modèle, sinon ça prendrait des semaines et beaucoup d'énergie!)
* code javascript :
  * On utilise la librairie `ml5` de p5.js pour la partie reconnaissance IA et la librairie `ubitwebusb.js` pour la communication avec le microbit
  * On propose des boutons pour connecter le microbit branché sur l'ordinateur
  * On charge le modèle précédemment entrainé
  * On affiche l'image obtenue par la camera
  * On fait une reconnaissance sur l'image obtenue
  * On affiche le resultat de la reconnaissance (plus facile pour débugger)
  * Si la reconnaissance est bonne pendant quelques secondes (pour éviter les bugs), on envoie le signal "IA" en serial au microbit branché sur l'ordinateur 


## Montage
Pour la guirlande, il s'agit de faire un deuxième interrupteur, en parallèle de celui associé au bouton. Ce deuxième interrupteur est contrôlé par le microbit de la guirlande.
Comme une guirlande fonctionne en 12V, il convient d'utiliser un transistor ou un mofset pour que le circuit 5V du microbit agisse sur le circuit 12V de la guirlande.
![Schéma de montage pour la guirlande](escapebox_4_avecia_schéma.png)

## Énigme
Lors de l'énigme précédente, on a obtenu une photo du père Noël (Paul, avec un bonnet !)
L'affiche précédente indiquait également qu'il faudrait se rendre sur une certaine page (https://divers.fannyboitard.fr/sem_noelpaulbonnet/ )
A cette page, on trouve le code javascript qui filme. Il faut lui montrer la photo du père Noël.
Si elle est reconnue, la guirlande s'allume !

## Eléments d'électronique et informatique travaillés
* Communication serie avec l'ordinateur
* Communication radio entre microbits
* Machine learning
* Javascript (p5.js)
* Hébergement d'une page web