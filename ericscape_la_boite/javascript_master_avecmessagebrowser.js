let msg = ""
let group = 0
let parts = []
let received = ""
let buffer = ""
let debug = true
radio.setGroup(23)
radio.on()
basic.forever(function () {
    received = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    if (received.includes(":")) {
        parts = received.split(":")
        group = parseInt(parts[0])
        msg = parts[1]
        debug = parts[2] === "debug"
        if (!(isNaN(group))) {
            radio.setGroup(group)
            radio.sendString("" + (msg))
            basic.showIcon(IconNames.Yes)
            basic.pause(500)
            if (debug) {
                basic.showString("" + (group))
                basic.showString("" + (msg))
            }
            basic.clearScreen()
        } else {
            basic.showIcon(IconNames.No)
            basic.pause(500)
            basic.clearScreen()
        }
    }
})

input.onButtonPressed(Button.A, function() {
    radio.setGroup(23)
    radio.sendString("sem")
})
