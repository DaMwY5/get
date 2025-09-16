import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]

n = 0
GPIO.setup(leds,GPIO.OUT)
up = 9
down = 10
GPIO.setup(up,GPIO.IN)
GPIO.setup(down,GPIO.IN)
GPIO.output(leds,0)
def dec2bin(value):
    return [int(element) for element in bin(value)[2::].zfill(8)]
sleep_time = 0.2
while True:
    if GPIO.input(up):
       n += 1 
       if n > 255:
        n = 255
    print(n,dec2bin(n))
    time.sleep(sleep_time)
    if GPIO.input(down):
       n -= 1 
       if n < 0:
        n = 0
    print(n,dec2bin(n))
    time.sleep(sleep_time)
    b = dec2bin(n)
    if GPIO.input(up) and GPIO.input(down):
        n = 255
        print(n,dec2bin(n))
        time.sleep(sleep_time)
    for i in range(8):
        GPIO.output(leds[i],b[i])