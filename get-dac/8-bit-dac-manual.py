import RPi.GPIO as GPIO
led = [16,20,21,25,26,17,27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)


dynamic_range = 3.3

def voltage_to_number(voltage):
    if not(0.0<=voltage<=dynamic_range):
        print(f"Напряжение выходит за динамчисекий диапозон ЦАП (0.00 - {dynamic_range:.2f} B")
        print("Устанавливаем 0.0В")
        return 0
    return int(voltage / dynamic_range * 255)


def dec2bin(value):
    return [int(element) for element in bin(value)[2::].zfill(8)]

def number_to_dac(number):
    b = dec2bin(number)
    for i in range(len(led)):
        GPIO.output(led[i],b[i])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число, Попробуйте ещё раз")
finally:
    GPIO.output(dac_bits,0)
    GPIO.cleanup()