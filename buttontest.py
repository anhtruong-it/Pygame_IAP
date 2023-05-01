import RPi.GPIO as GPIO
import time

button_pin = [17, 23, 24, 25]
led_pin = 8
print("ok")
def button_callback(channel):
    #print("Button {} pressed".format(channel))
    if channel == 17:
        button_name = "Right"
        #GPIO.output(led_pin, GPIO.HIGH)
        print("led on")
    elif channel == 23:
        button_name = "Down"
    elif channel == 24:
        button_name = "Left"
    elif channel == 25:
        button_name = "Up"
    
    #print("Button {} pressed".format(button_name))
    while GPIO.input(channel) == GPIO.HIGH:
        print("Button {} pressed".format(button_name))
        if button_name == "Right":
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(0.05)
            print("led on")
        time.sleep(0.1)
    print("Button {} released".format(button_name))
    GPIO.output(led_pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)
for pin in button_pin:
    GPIO.add_event_detect(pin, GPIO.RISING, callback=button_callback, bouncetime=200)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

