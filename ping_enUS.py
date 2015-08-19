#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledtest = 2 # Turns on while pinging
ledNOK = 3 # Turns on if the ping response is an error
ledOK = 4 # Turns on if there is a ping response

GPIO.setup(ledtest, GPIO.OUT)
GPIO.setup(ledNOK, GPIO.OUT)
GPIO.setup(ledOK, GPIO.OUT)

print "Testing the leds"
GPIO.output(ledtest, 1)
time.sleep(0.1)
GPIO.output(ledtest, 0)
GPIO.output(ledNOK, 1)
time.sleep(0.1)
GPIO.output(ledNOK, 0)
GPIO.output(ledOK, 1)
time.sleep(0.1)
GPIO.output(ledOK, 0)
print "Tested"

url=raw_input("Site:")
intervalo=input("Interval (seconds):")
tenta=input("Attempts (how many times the script pings):")
cont=0

while cont < tenta:
	time.sleep(intervalo)
	# this ping part below is based on the answer of user 10flow as posted on http://stackoverflow.com/questions/2953462/pinging-servers-in-python
	print ""
	print "Attempt " + str(cont+1) 
	print ""
	GPIO.output(ledNOK, 0)
	GPIO.output(ledOK, 0)
	GPIO.output(ledtest, 1)
	import os
	hostname = url #example
	response = os.system("ping -c 1 " + hostname)
	GPIO.output(ledtest, 0)
	#and then check the response...
	if response == 0:
		GPIO.output(ledNOK, 0)
		GPIO.output(ledOK, 1)
		time.sleep(0.1)
		GPIO.output(ledOK, 0)
		time.sleep(0.1)
		GPIO.output(ledOK, 1)
		time.sleep(0.1)
		GPIO.output(ledOK, 0)
		time.sleep(0.1)
		GPIO.output(ledOK, 1)
		time.sleep(0.1)
		GPIO.output(ledOK, 0)
		time.sleep(0.1)
		GPIO.output(ledOK, 1)
		time.sleep(0.1)
		GPIO.output(ledOK, 0)
		time.sleep(0.1)
		GPIO.output(ledOK, 1)
		time.sleep(0.1)
		GPIO.output(ledOK, 0)
		time.sleep(0.1)
		GPIO.output(ledOK, 1)

	else:
		GPIO.output(ledOK, 0)
		GPIO.output(ledNOK, 1)
		time.sleep(0.1)
		GPIO.output(ledNOK, 0)
		time.sleep(0.1)
		GPIO.output(ledNOK, 1)
		time.sleep(0.1)
		GPIO.output(ledNOK, 0)
		time.sleep(0.1)
		GPIO.output(ledNOK, 1)
		time.sleep(0.1)
		GPIO.output(ledNOK, 0)
		time.sleep(0.1)
		GPIO.output(ledNOK, 1)
		time.sleep(0.1)
		GPIO.output(ledNOK, 0)
		time.sleep(0.1)
		GPIO.output(ledNOK, 1)
		time.sleep(0.1)
		GPIO.output(ledNOK, 0)
		time.sleep(0.1)
		GPIO.output(ledNOK, 1)
	cont=cont+1
else:
	GPIO.output(ledOK, 0)
	GPIO.output(ledNOK, 0)
	print ""
	print "Ended!"
