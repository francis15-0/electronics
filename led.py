from gpiozero import LED
from time import sleep
from gpiozero import DistanceSensor

sensor = DistanceSensor(20, 21)
red = LED(16)
yellow = LED(12)
while True:
    sen = sensor.distance * 100
    print(sensor.distance * 100)
    if(sen >= 50):
        red.on()
        sleep(1)
        red.off()
        yellow.on()
        sleep(1)
        yellow.off()
    else:
        red.off()
        yellow.off()
    sleep(1)   
