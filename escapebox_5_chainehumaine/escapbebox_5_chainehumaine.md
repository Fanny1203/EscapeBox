# Escape Box - Enigme Chaine Humaine - animation ordinateur

[![Miniature vidéo](https://img.youtube.com/vi/kynYglUlyQ0/0.jpg)](https://www.youtube.com/watch?v=kynYglUlyQ0)

## Description
Un petit robot tend ses mains : il faut les lui tenir et former une "chaine humaine".
Cette chaine humaine est détectée par un microbit qui envoie un message en série à l'ordinateur auquel il est connecté.
Une page web (en javascript) ouverte écoute la série et déclenche une animation quand le microbit a envoyé le message.
Remarque: si on veut éviter que le robot soit branché à l'ordinateur, on peut, comme pour les projets qui précèdent, utiliser deux microbits, l'un qui détecte la chaine humaine et envoie un message radio. L'autre qui recoit le message radio et le propage en communiquant en série avec l'ordinateur.


## Matériel nécessaire
Un ordinateur avec un  microbit branché (communication série entre l'ordinateur et le microbit)
Sur l'ordinateur, la page web qui écoute la série et peut déclencher une animation.


## Montage
Presque rien à monter ! Un fil qui part du pin 0 du microbit et un autre qui part du ground. Quand le circuit est fermé par la chaine humaine, le microbit le détecte (fonction spéciale: `is_touched()` )

## Énigme
L'affiche indique comment faire la correspondance, et dans quel ordre.
![Affiche de l'énigme](escapebox_5_chainehumaine_affiche.png)




