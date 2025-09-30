import RPi.GPIO as GPIO
led = [16,20,21,25,26,17,27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        # Инициализация GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
        

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()


    def set_number(self, number):
        """
        Установка числа на вход R2R-ЦАП
        
        Args:
            number (int): Число от 0 до 255
        """
        if number < 0 or number > 255:
            raise ValueError("Число должно быть в диапазоне 0-255")
        
        # Преобразование числа в двоичное представление
        binary = format(number, '08b')
        
        # Установка состояния каждого пина
        for i, pin in enumerate(self.gpio_bits):
            bit_value = int(binary[7 - i])  # Старший бит первый в списке пинов
            GPIO.output(pin, bit_value)
        
        if self.verbose:
            print(f"Число на вход ЦАП: {number} биты: {binary})")

    def set_voltage(self, voltage):

        if voltage < 0 or voltage > self.dynamic_range:
            raise ValueError(f"Напряжение должно быть в диапазоне 0.0-{self.dynamic_range} В")
        
        # Расчет числа для ЦАП
        number = int((voltage / self.dynamic_range) * 255)
        
        # Ограничение до 255
        number = min(number, 255)
        
        
        self.set_number(number)


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                print()
                
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    
    finally:
        dac.deinit()