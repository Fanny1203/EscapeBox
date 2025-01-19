from microbit import *
import radio
#radio
radio.config(group=23)
radio.on()

uart.init(baudrate=115200)  
msg_str=""

while True:  
    msg_bytes = uart.read() # Lire les données de l'UART  
    if msg_bytes:  
        # Convertir en string et supprimer les sauts de ligne  
        msg_str = str(msg_bytes, 'utf-8').strip()
        display.show(Image.HAPPY) #pour voir que c'est bon
        radio.send("IA")
        sleep(1000)
        display.clear()