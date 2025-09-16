import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led,GPIO.OUT)
state = 0
period = 0.5
port = 6
GPIO.setup(port,GPIO.IN)
while True:
    input_state = GPIO.input(port)
    GPIO.output(led,not input_state)
    
    
    
    
    
    
    
    
    
    


# hfjghfjfhkjf