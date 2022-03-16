import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 250)
try:
    while 1:
        
        print("Введите скважность")
        var = int(input())
        p.start(var)
        input('Press return to stop:')   # use raw_input for Python 2
        p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()