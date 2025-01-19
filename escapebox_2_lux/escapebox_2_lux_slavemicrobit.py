from microbit import *
import radio

radio.on()
radio.config(group=23)

servo = pin0

def rotate_servo():
    for angle in range(0, 180, 10):
        servo.write_analog(angle)
        sleep(15)

# Main program loop
while True:
    reception = radio.receive()
    if reception == "lux":
        rotate_servo()
    sleep(100)