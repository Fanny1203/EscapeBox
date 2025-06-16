input.onButtonPressed(Button.A, function () {
    envoyermessageradio("boite1")
})
function envoyermessageradio (texte: string) {
    basic.showIcon(IconNames.Heart)
    radio.sendString("boite1")
    basic.pause(500)
    basic.clearScreen()
}
input.onButtonPressed(Button.B, function () {
    envoyermessageradio("sem")
})
radio.setGroup(23)
