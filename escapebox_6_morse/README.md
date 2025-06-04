# Escape Box - Enigme Morse - animation ordinateur

[![Miniature vidéo](https://img.youtube.com/vi/VOTRE_ID_VIDEO/0.jpg)](https://www.youtube.com/watch?v=VOTRE_ID_VIDEO)

## Description
Un microbit détecte des appuis sur un bouton et les traduit en code morse. Si le code entré correspond au code attendu, on envoi un message radio pour déclencher l'ouverture d'une boite

## Autres versions prévues
- Ouverture d'une "boite à bonbon".
- Dans le code, tenir compte des pauses et reconnaitre à chaque grande pause la lettre qui vient d'être codée. Comparer les lettres entrées en morse aux lettres du code.
- Dans le code, mémoriser tous les temps d'appuis. A chaque grande pause, faire une analyse statistique pour reconnaitre les appuis courts/longs. Pour cette "analyse", on pourrait tenir compte du plus grand écart dans le temps pour discriminer le groupe des courts et le groupe des longs
- Remarque : en indiquant avec un indice sonore et/ou visuel qu'on vient d'entrer un point (bip court / point affiché) ou un tiret (bip long / trait affiché), on peut éviter à mon avis de faire l'analyse statistique précédemment suggérée. L'ergonomie permet à l'utilisateur d'adapter le temps d'appui. Tester le 17 avril, ça a marché du premier coup avec les personnes cobayes !

## Matériel nécessaire
* Un bouton poussoir
* Des fils de connexion
* Un microbit qui lit le morse / un microbit qui ouvre la boite, ou un seul pour les deux (à développer, compatible avec une boite à bonbons pour laquelle le microbit reste accessible à l'extérieur ou avec une ericscape en plaçant le bouton pression sur la boite et en le branchant avec le microbit qui est à l'intérieur)

## Montage
* Pour l'instant, le bouton pressoir est le bouton A intégré au microbit

## Énigme
Cette énigme fait partie de l'enter game du SEM. Les participants ont trouvé 3 lettres, qu'ils ont traduites à l'aide d'une roue de César et qu'ils doivent maintenant communiquer en morse.