input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    ouverture()
    basic.clearScreen()
})
function ouverture () {
    servos.P0.setStopOnNeutral(true)
    servos.P0.setAngle(angle_ouvert)
    basic.pause(1000)
    servos.P0.setAngle(angle_ferme)
    basic.pause(1000)
    servos.P0.setStopOnNeutral(false)
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "sem" || receivedString == nomboite) {
        basic.showIcon(IconNames.Happy)
        ouverture()
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString(nomboite)
})
let nomboite = ""
let angle_ouvert = 0
let angle_ferme = 0
radio.setGroup(23)
servos.P0.setStopOnNeutral(true)
angle_ferme = 5
angle_ouvert += 40
nomboite = "boite40"
servos.P0.setAngle(angle_ferme)
servos.P0.setStopOnNeutral(false)
