#!/usr/bin/env python
#-*- coding: utf-8 -*-

import serial
import time

def send_message(numero,mensaje):
	ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
	print ('Enviando mensaje ...')
	ser.write('AT+CMGF=1\r\n')
	#print(ser.read(100))
	time.sleep(1)
	ser.write('AT+CSCS="8859-1"\r\n')
	#print(ser.read(100))
	time.sleep(1)
	ser.write('AT+CMGS="'+numero+'"\r\n')
	#print(ser.read(100))
	time.sleep(1)
	ser.write(mensaje)
	#print(ser.read(100))
	time.sleep(1)
	#ser.write('+CMGS: 198 \r\n')
	ser.write('\x1a')
	#print(ser.read(100))
        ser.close()
	print ('Mensaje enviado :)')
