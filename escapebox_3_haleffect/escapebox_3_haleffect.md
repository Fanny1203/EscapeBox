# Escape Box - Enigme Aimants

[![Miniature vidéo](https://img.youtube.com/vi/2xihjn7eewY/0.jpg)](https://www.youtube.com/watch?v=2xihjn7eewY)

## Description
Sur une boite séparée, des capteurs magnétiques sont installés. 
S'ils captent des aimants, dans un ordre particulier, le microbit associé envoie le signal "aimant".
La boite *ericscape* s'ouvre si elle reçoit ce signal.

On pose des plaquettes sur la boite à des emplacements prévus.
Les aimants se trouvent sur ces plaquettes, décentrés. 
Il faut donc que les plaquettes recouvrent les bons emplacements de la boite pour que les aimants soient alignés avec les capteurs.


## Matériel nécessaire
* Une [ericscape](../ericscape_la_biote/ericscape.md)
* Une boite en bois
* Deux microbits (un master, un slave)
* Trois capteurs hal-effect avec résistances et led intégrées:
  * dans le commerce https://sensorkit.joy-it.net/fr/sensors/ky-003
  * Ou les capteur que nous avons conçus:
![Capteur maison](escapebox_3_haleffect_capteurpcb.png)

## Remarques sur le code
On commence par lire la lumière ambiante 500 fois et on en tire une valeur médiane.
On compare ensuite les valeurs des capteurs à cette valeur médiane pour déterminer s'ils sont éclairés.
On calcule pour cela la différence relative `(lecture-médiane)/mediane`. 
Le taux de différence pour décider qu'il y a un changement est paramétrable dans le code (lors de la réalisation initiale, on avait choisi 10%).
Une particularité du code, c'est qu'on veut que les capteurs détectent les aimants dans un ordre précis. 
On mémorise donc dans une liste la suite des index des capteurs qui sont passés de off à on.

## Montage
On recommande l'utilisation de capteurs à effet hal incluant déjà des résistances et une led qui s'allume en cas de détection d'un signal magnétique.
Dans ce cas, il suffit de brancher les capteurs sur les pins 0, 1 et 2 du microbit "master".

## Énigme
L'affiche indique comment faire la correspondance, et dans quel ordre.
![Affiche de l'énigme](escapebox_3_haleffect_affiche.png)

## Eléments d'électronique et informatique travaillés
* Capteurs à effet hal
* Analyse de données
* Communication radio entre microbits
* Ericscape: servo moteur, impression 3D