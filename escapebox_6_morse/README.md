# Escape Box - Enigme Morse - animation ordinateur

[![Miniature vidéo](https://img.youtube.com/vi/VOTRE_ID_VIDEO/0.jpg)](https://www.youtube.com/watch?v=VOTRE_ID_VIDEO)

## Description
Un microbit détecte des appuis sur un bouton et les traduit en code morse. Les messages en morse sont envoyés en série à l'ordinateur auquel il est connecté.
Une page web (en javascript) écoute la série et déclenche une animation quand le microbit a envoyé le bon message en morse.

## Suggestion d'amélioration
Comme pour les projets qui précèdent, on peut utiliser deux microbits, l'un qui détecte les appuis et envoie un message radio, l'autre qui reçoit le message radio et le propage en communiquant en série avec l'ordinateur.

## Matériel nécessaire
* Un ordinateur avec un microbit branché (communication série entre l'ordinateur et le microbit)
* Sur l'ordinateur, la page web qui écoute la série et peut déclencher une animation
* Un bouton poussoir
* Des fils de connexion
* Une breadboard

## Montage
* Le bouton poussoir est connecté au pin 0 du microbit
* Quand le bouton est pressé, le microbit détecte l'appui et mesure sa durée pour déterminer s'il s'agit d'un point ou d'un tiret en morse
* Les appuis sont traduits en morse et envoyés via la communication série

## Partie javascript
* On utilise la librairie `ubitwebusb.js` pour la communication avec le microbit
* On propose des boutons pour connecter le microbit branché sur l'ordinateur
* Si on reçoit le bon message en morse via la communication série, on affiche l'animation

## Énigme
L'affiche indique qu'il faut transmettre un message secret en morse. En appuyant sur le bouton selon le code morse approprié, on déclenche l'animation sur l'ordinateur qui révèle l'indice suivant.
