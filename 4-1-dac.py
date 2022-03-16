import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    print("Напишите целое число в диапазоне от 0 до 255:")
    input_value = int(input())

    if input_value > 255:
        print("Некорректный ввод")

    if input_value < 0:
        print("Некорректный ввод")

    currency = input_value/256 * 3.3
    print("Напряжение:", currency, "В")

    GPIO.output(dac, decimal2binary(input_value))
    
    time.sleep(5)


except ArithmeticError:
    value = 0

else:
    print("No exceptions")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()