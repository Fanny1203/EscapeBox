# Escape Box - Enigme IA-guirlande

[![Miniature vidéo](https://img.youtube.com/vi/AJQ-Y7U1JHs/0.jpg)](https://www.youtube.com/watch?v=AJQ-Y7U1JHs)

## Description
Sur un ordinateur, une page Internet est affichée avec une camera filme. 
Si la bonne image est montrée à la camérapendant quelques secondes, un microbit branché sur l'ordinateur envoie un signal "IA".
Un autre microbit déclanche la guirlande lorsqu'il recoit le signal "IA".



## Matériel nécessaire
Un ordinateur avec un premier microbit branché (communication série entre l'ordinateur et le microbit)
Un modèle de reconnaissance d'images pré-entrainé à reconnaitre une image en particulier (par exemple avec teachable machine : https://teachablemachine.withgoogle.com/train)
Sur l'ordinateur, la page web qui filme et fait analyser l'image par le modèle
Un deuxième microbit branché à la guirlande (voir schéma de montage)

## Montage
Pour la guirlande, il s'agit de faire un deuxième interrupteur, en parallèle de celui associé au bouton. Ce deuxième interrupteur est contrôlé par le microbit de la guirlande.
Comme une guirlande fonctionne en 12V, il convient d'utiliser un transistor ou un mofset pour que le circuit 5V du microbit agisse sur le circuit 12V de la guirlande.
![Schéma de montage pour la guirlande](escapebox_4_avecia_schéma.png)

## Énigme
L'affiche précédente indiquait les informations (avec l'image obtenue, aller à telle adresse et faire une reconnaissance pour faire allumer la guirlande)


