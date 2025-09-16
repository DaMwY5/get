import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led,GPIO.OUT)
state = 0
period = 0.5
pwm = GPIO.PWM(led,200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty+=10.0
    if duty > 300.0:
        duty = 0.0