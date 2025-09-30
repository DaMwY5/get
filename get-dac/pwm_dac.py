import RPi.GPIO as GPIO

led = [16,20,21,25,26,17,27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
  
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0) 
        
    def deinit(self):

        if self.pwm is not None:
            self.pwm.stop()
        
        GPIO.cleanup()
        

    def set_voltage(self, voltage):
 
        if voltage < 0 or voltage > self.dynamic_range:
            raise ValueError(f"Напряжение должно быть в диапазоне 0.0-{self.dynamic_range} В")

        duty_cycle = (voltage / self.dynamic_range) * 100
        duty_cycle = min(duty_cycle, 100.0)
        self.pwm.ChangeDutyCycle(duty_cycle)



if __name__ == "__main__":
    try:

        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                print()  
                
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        dac.deinit()