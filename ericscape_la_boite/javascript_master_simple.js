// variables du projet
let group = 23
let message = "boite1"
let debug = true

radio.setGroup(group)

input.onButtonPressed(Button.A, function () {
    envoyermessageradio(message)
})

input.onButtonPressed(Button.B, function () {
    envoyermessageradio("sem")
})

function envoyermessageradio (texte: string) {
    basic.showIcon(IconNames.Heart)
    radio.on()
    radio.sendString(texte)
    basic.pause(500)
    radio.off()
    basic.clearScreen()
}
