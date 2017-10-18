#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import datetime
from encode import encode_msg, encode_phn
from send_message import send_message
import pyodbc


today = datetime.datetime.today().strftime('%Y-%m-%d')

#conn = pyodbc.connect(driver = 'FreeTDS', server = 'GEDEON.HACFSA.ORG.AR', port = 1433,	database = 'MHO_QA', uid = 'prueba', pwd = 'prueba')
conn = pyodbc.connect(driver = 'FreeTDS', server = 'MANA1.HACFSA.ORG.AR', port = 1433,	database = 'MHO', uid = 'sms', pwd = 'Sms@telefonia')

print 'Conectado a la base de datos ...'
cursor = conn.cursor()
cursor.execute("exec SMS_turnos_sp")
turns = []
arr = []

for i in cursor:
	phone = i[0]
	orderly_turn = i[1]
	date = i[2]
	hour = i[3]
	speciality = i[4]
	arr = (phone, orderly_turn, date, hour, speciality)
	turns.extend([arr])

print 'Se registran ' + str(len(turns)) + ' turnos.'
#cursor.execute("exec SMS_mensajeenviado_alta_sp 1, '3704713781', 'asdfasd', '2017-01-01'")


for turn in turns:
	#phone = encode_phn(turn[0]) Se comento la codificacion de UCS2 para utilizar 8859-1
	phone = turn[0]
	#message = encode_msg('Recordatorio Turnos HAC - Fecha: ' + turn[2] + ' Hora: ' + turn[3] + 'HS. Especialidad: ' + turn[4] + '. No responda este mensaje.')
	message = 'Recordatorio Turnos HAC - Fecha: ' + turn[2] + ' Hora: ' + turn[3] + 'HS. Especialidad: ' + turn[4] + '. No responda este mensaje.'
	time.sleep(5)
	send_message(phone, message)
        print "exec SMS_mensajeenviado_alta_sp " + str(turn[1]) + ",'" + str(turn[0]) + "','" + message + "','" + str(today) + "'"
	cursor.execute("exec SMS_mensajeenviado_alta_sp " + str(turn[1]) + ",'" + str(turn[0]) + "','" + message + "','" + str(today) + "'")
        conn.commit()


