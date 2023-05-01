import RPi.GPIO as GPIO
import time
button_pin = 17
button_state = False
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_pin = 22
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, GPIO.LOW)

while True:
	new_button_state = GPIO.input(button_pin)
	
	if new_button_state == False and button_state == True:
		count += 1
		print("Button pressed {} time".format(count))
		if count % 2 == 0:
			print("led off")
			GPIO.output(led_pin, GPIO.LOW)
		else:
			print("led on")
			GPIO.output(led_pin, GPIO.HIGH)
			 
	button_state = new_button_state
	

