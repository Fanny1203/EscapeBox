// Pour que ce code soit fonctionnel, ajouter la librairie servo. Pour cela, aller sur l'engrenage en haut à droite puis "extensions" et chercher "servo"


// variables du projet
let nomboite = "boite1"
let nomgenerique = "sem"
let angle_ouvert = 40
let angle_ferme = 5
let group_radio = 23


radio.setGroup(group_radio)
servos.P0.setStopOnNeutral(true)
servos.P0.setAngle(angle_ferme)
servos.P0.setStopOnNeutral(false)
radio.on()

input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    ouverture()
    basic.clearScreen()
})

input.onButtonPressed(Button.B, function () {
    basic.showString(nomboite)
})

radio.onReceivedString(function (receivedString) {
    if (receivedString == nomgenerique || receivedString == nomboite) {
        basic.showIcon(IconNames.Happy)
        ouverture()
        basic.clearScreen()
    }
})


function ouverture () {
    servos.P0.setStopOnNeutral(true)
    servos.P0.setAngle(angle_ouvert)
    basic.pause(1000)
    servos.P0.setAngle(angle_ferme)
    basic.pause(1000)
    servos.P0.setStopOnNeutral(false)
}