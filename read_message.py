
import serial
import time

def read_message(num):
	ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
	print ('Leyendo mensajes ...')
	ser.write('AT+CMGR=' + num + '\r\n')
	msg = ser.read(1000)
	ser.close()
	return msg


