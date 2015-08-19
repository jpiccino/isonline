#!/usr/bin/python
# coding=<UFT-8>

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledtest = 2 # Liga durante o ping
ledNOK = 3 # Liga se nao tiver resposta
ledOK = 4 # Liga se tiver resposta

GPIO.setup(ledtest, GPIO.OUT)
GPIO.setup(ledNOK, GPIO.OUT)
GPIO.setup(ledOK, GPIO.OUT)

print "Testando os leds"
GPIO.output(ledtest, 1)
time.sleep(0.1)
GPIO.output(ledtest, 0)
GPIO.output(ledNOK, 1)
time.sleep(0.1)
GPIO.output(ledNOK, 0)
GPIO.output(ledOK, 1)
time.sleep(0.1)
GPIO.output(ledOK, 0)
print "Testado"

url=raw_input("Site ou IP:")
intervalo=input("Intervalo (seg):")
tenta=input("Numero de tentativas:")
cont=0

while cont < tenta:
	# this ping part below is based on the answer of user 10flow as posted on http://stackoverflow.com/questions/2953462/pinging-servers-in-python
	print ""
	print "Tentativa " + str(cont+1) 
	print ""
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
	time.sleep(intervalo)
	cont=cont+1
else:
	GPIO.output(ledOK, 0)
	GPIO.output(ledNOK, 0)
	print ""
	print "Acabou!"
