# L'ericscape

[Démo en vidéo](https://youtu.be/baRv0PoeU1Q)

## Genèse
En général les boites d'escape game fonctionnent avec des élектro-aimants: ces aimants sont alumés par défaut et sont éteints quand la bonne action est entreprise, permetant l'ouverture de la boite. C'est un peu dommage d'avoir ce fonctionnnement "on" par défaut et nous avons réfléchi à une boite qui fonctionnerait au contraire en étant fermée "au repos" et qui a besoin d'alimentation pour s'ouvrir.


## Cahier des charges de la serrure
La boite devait répondre aux exigences suivantes:
- être fermée par défaut, avoir besoin d'énergie seulement pour s'ouvrir
- avoir un système de "secours" pour qu'on l'ouvre s'il y a un problème
- intégrer un microbit qui déclenche l'ouverture à la réception d'un signal radio
- l'ouverture doit être visible (le couvercle doit se soulever). C'est important dans le cadre d'un jeu de type escape game, pour que les joueurs s'apercevent que quelque chose s'est passé.

## Schéma de la serrure
Eric a concu une serrure qui s'ouvre avec un servo moteur. 
![Serrure](ericscape_serrure1.jpg)

Cette serrure est montée de sorte de pouvoir être ouverte par un servo moteur commandé par un microbit ou par l'insersion d'un trombone dans un trou discret sous la boite.
Un élastique assure le côté "pop" de l'ouverture.
Cette serrure est imprimable en 3D.

## Matériel
- Boite : dimensions 20x8,5x7,5cm
Nous avons utilisé: [celle-ci](https://www.galaxus.ch/fr/s5/product/glorex-boite-rectangle-20x85x75cm-fsc-fournitures-pour-loisirs-creatifs-12930330)
Mais [cette autre] (https://www.galaxus.ch/fr/s5/product/i-am-creative-boite-en-bois-coffre-au-tresor-coffre-a-bijoux-fournitures-pour-loisirs-creatifs-22898985) 
pourrait aussi servir en diminuant de quelques milimètres la hauteur de la gachette 
- Serrure imrimée en 3D (cf fichiers ci-dessous)
- Servomoteur de type SG90 ou SG92R, sur [berrybase](https://www.berrybase.ch/sg92r-micro-servo)
- Microbit décembre 2018, avec boitier alimentation 3V inclus : sur [berrybase](https://www.berrybase.ch/en/bbc-micro-bit-v2.21-go-bundle)
- Elastiques dentaires (vous en trouverez gratuitement chez les orthodentistes ! Sinon en vente [ici](https://www.fruugoschweiz.com/10packs-1000pcs-elastique-dentaire-elastique-bandes-orthodontiques-35oz-5oz-65oz-produit-orthodontique-dentaire/p-172381001-368495361?language=fr&ac=bing))
- Boitier alimentation 5V avec 4 piles AA: sur [berrybase](https://www.berrybase.ch/en/batteriehalter-fuer-4x-mignon-aa-mit-150mm-anschlusskabel-geschlossenem-gehaeuse-und-schalter-wasserabweisend)

![Boite](ericscape_boite.jpg)



## Fichiers pour impression 3D
Le projet est accessible sur onshape [onshape](https://cad.onshape.com/documents/3392f1d195d84b6c0f49f3b8/w/7acc2ea9644cbdbbe5b3fe8c/e/d5a02ecf17d01a1ba5a197bc)
Le fichier est accessible en lecture à toute personne connectée. Il est alors possible de le télécharger au format STL pour l'imprimer.


## Montage électronique
Alimenter le microbit en 3V et le servo moteur en au moins 5V.
Le fil  "controle" du servo moteur est branché directement au microbit, qui écrira en analogique.
Tous les ground (microbit, alim 5V et ground du servo moteur) doivent être reliés (alim 3V via connecteur alimentation, relié également automatiquement).

## Gestion du servo moteur

En mode analogique, on a des pulsations régulères (toutes les 20 ms).
Cela peut dépenser de l'énergie inutilement puisqu'on a uniquement besoin de "pousser" quand on ouvre.
Deux solutions pour economiser dans les moments où on n'utilise pas le servo moteur:
- changer la période de pulsations
- passer en digital
On constate bien la différence: le servo moteur n'exercice pas de résistance si on essaye de le pousser quand il est "au repos"


## Eléments d'électronique et informatique travaillés
* Design et impression 3D
* Gestion d'un servo moteur
* (Beaucoup de bricolage !)


[def]: https://cad.onshape.com/documents/3392f1d195d84b6c0f49f3b8/w/7acc2ea9644cbdbbe5b3fe8c/e/d5a02ecf17d01a1ba5a197bc