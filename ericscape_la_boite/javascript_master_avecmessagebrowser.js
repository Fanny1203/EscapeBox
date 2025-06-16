let msg = ""
let group = 0
let parts = []
let received = ""
let buffer = ""
let debug = true
radio.setGroup(23)

basic.forever(function () {
    // on lit la première ligne du message série de la page web, qui est sous la forme groupe:message:debug
    received = serial.readUntil(serial.delimiters(Delimiters.NewLine)) 
    if (received.includes(":")) {
        parts = received.split(":") 
        group = parseInt(parts[0])
        msg = parts[1]
        debug = parts[2] === "debug"
        if (!(isNaN(group))) {
            envoyermessage(group, msg)
            basic.clearScreen()
        } else {
            basic.showIcon(IconNames.No)
            basic.pause(500)
            basic.clearScreen()
            if(debug){
                basic.showString("groupe invalide")
                basic.showString(""+group)
            }
        }
        basic.clearScreen()
    }
})

input.onButtonPressed(Button.A, function() {
    envoyermessage(23, "sem")
})

function envoyermessage(group : number, msg : string) {
    radio.setGroup(group)
    radio.on()
    radio.sendString(msg)
    basic.showIcon(IconNames.Yes)
    basic.pause(500)
    basic.clearScreen()
    radio.off()
    if (debug) {
        basic.showString("gp:"+group)
        basic.showString("msg:"+msg)
    }
}
