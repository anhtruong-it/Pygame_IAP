import RPi.GPIO as GPIO
import time
states = 1
GPIO.setmode(GPIO.BCM)
		# [29, 31, 36, 37]
led_pin = [5, 6, 16, 26]
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin[0], GPIO.LOW)
GPIO.output(led_pin[1], GPIO.LOW)
GPIO.output(led_pin[2], GPIO.LOW)
GPIO.output(led_pin[3], GPIO.LOW)
# button_pin = [11, 16, 18, 22]
button_pin = [17, 23, 24, 25]
state = False
state_2 = False
state_3 = False
button_state_0 = False
button_state_1 = False
button_state_2 = False
button_state_3 = False
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
	new_button_state_0 = GPIO.input(button_pin[0])
	new_button_state_1 = GPIO.input(button_pin[1])
	new_button_state_2 = GPIO.input(button_pin[2])
	new_button_state_3 = GPIO.input(button_pin[3])
	if count < 4:
		if not state:
			GPIO.output(led_pin[0], GPIO.HIGH)
			GPIO.output(led_pin[1], GPIO.HIGH)
			GPIO.output(led_pin[2], GPIO.HIGH)
			GPIO.output(led_pin[3], GPIO.HIGH)

		if new_button_state_0 == False and button_state_0 == True:
			count_0 += 1
			state = True
			print("Button pressed {} time".format(count_0))
			if count_0 % 2 != 0:
				print("led off")
				GPIO.output(led_pin[0], GPIO.LOW)
				count += 1
				
		if new_button_state_1 == False and button_state_1 == True:
			count_1 += 1
			state = True
			print("Button pressed {} time".format(count_1))
			if count_1 % 2 != 0:
				print("led off")
				GPIO.output(led_pin[1], GPIO.LOW)
				count += 1
		if new_button_state_2 == False and button_state_2 == True:
			count_2 += 1
			state = True
			print("Button pressed {} time".format(count_2))
			if count_2 % 2 != 0:
				print("led off")
				GPIO.output(led_pin[2], GPIO.LOW)
				count += 1
		if new_button_state_3 == False and button_state_3 == True:
			count_3 += 1
			state = True
			print("Button pressed {} time".format(count_3))
			if count_3 % 2 != 0:
				print("led off")
				GPIO.output(led_pin[3], GPIO.LOW)
				
				count += 1
			 
		button_state_0 = new_button_state_0
		button_state_1 = new_button_state_1
		button_state_2 = new_button_state_2
		button_state_3 = new_button_state_3
	
	elif 4<= count <=7:
		if not state_2:
			time.sleep(2)
			count_0 = 0
			count_1 = 0
			count_2 = 0
			count_3 = 0
			button_state_0 = False
			button_state_1 = False
			button_state_2 = False
			button_state_3 = False
			GPIO.output(led_pin[0], GPIO.HIGH)
			GPIO.output(led_pin[1], GPIO.HIGH)
			GPIO.output(led_pin[2], GPIO.HIGH)
			GPIO.output(led_pin[3], GPIO.HIGH)
			time.sleep(3)
			GPIO.output(led_pin[0], GPIO.LOW)
			GPIO.output(led_pin[1], GPIO.LOW)
			GPIO.output(led_pin[2], GPIO.LOW)
			GPIO.output(led_pin[3], GPIO.LOW)
			state_2 = True
		
		
		if new_button_state_0 == False and button_state_0 == True:
			count_0 += 1
			print("Button pressed {} time".format(count_0))
			if count_0 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[0], GPIO.HIGH)
				count += 1
				
		if new_button_state_1 == False and button_state_1 == True:
			count_1 += 1
			print("Button pressed {} time".format(count_1))
			if count_1 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[1], GPIO.HIGH)
				count += 1
				
		if new_button_state_2 == False and button_state_2 == True:
			count_2 += 1
			print("Button pressed {} time".format(count_2))
			if count_2 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[2], GPIO.HIGH)
				count += 1
				
		if new_button_state_3 == False and button_state_3 == True:
			count_3 += 1
			print("Button pressed {} time".format(count_3))
			if count_3 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[3], GPIO.HIGH)
				count += 1
			 
		button_state_0 = new_button_state_0
		button_state_1 = new_button_state_1
		button_state_2 = new_button_state_2
		button_state_3 = new_button_state_3
	
	elif 8 <= count < 12:
		if not state_3:
			time.sleep(1)
			GPIO.output(led_pin[0], GPIO.LOW)
			GPIO.output(led_pin[1], GPIO.LOW)
			GPIO.output(led_pin[2], GPIO.LOW)
			GPIO.output(led_pin[3], GPIO.LOW)
			time.sleep(2)
			count_0 = 0
			count_1 = 0
			count_2 = 0
			count_3 = 0
			button_state_0 = False
			button_state_1 = False
			button_state_2 = False
			button_state_3 = False
			GPIO.output(led_pin[2], GPIO.HIGH)
			time.sleep(2)
			GPIO.output(led_pin[1], GPIO.HIGH)
			time.sleep(2)
			GPIO.output(led_pin[3], GPIO.HIGH)
			time.sleep(2)
			GPIO.output(led_pin[0], GPIO.HIGH)
			time.sleep(2)
			GPIO.output(led_pin[0], GPIO.LOW)
			GPIO.output(led_pin[1], GPIO.LOW)
			GPIO.output(led_pin[2], GPIO.LOW)
			GPIO.output(led_pin[3], GPIO.LOW)
			state_3 = True
		
		
		if new_button_state_0 == False and button_state_0 == True and count == 11:
			count_0 += 1
			print("Button pressed {} time".format(count_0))
			if count_0 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[0], GPIO.HIGH)
				count += 1
				
		if new_button_state_1 == False and button_state_1 == True and count == 9:
			count_1 += 1
			print("Button pressed {} time".format(count_1))
			if count_1 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[1], GPIO.HIGH)
				count += 1
				
		if new_button_state_2 == False and button_state_2 == True and count == 8:
			count_2 += 1
			print("Button pressed {} time".format(count_2))
			if count_2 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[2], GPIO.HIGH)
				count += 1
				
		if new_button_state_3 == False and button_state_3 == True and count == 10:
			count_3 += 1
			print("Button pressed {} time".format(count_3))
			if count_3 % 2 != 0:
				print("led oN")
				GPIO.output(led_pin[3], GPIO.HIGH)
				count += 1
			 
		button_state_0 = new_button_state_0
		button_state_1 = new_button_state_1
		button_state_2 = new_button_state_2
		button_state_3 = new_button_state_3
	
	
	else:
		time.sleep(2)
		GPIO.output(led_pin[0], GPIO.LOW)
		GPIO.output(led_pin[1], GPIO.LOW)
		GPIO.output(led_pin[2], GPIO.LOW)
		GPIO.output(led_pin[3], GPIO.LOW)
	
	
	
	
GPIO.cleanup()
