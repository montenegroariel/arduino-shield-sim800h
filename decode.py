#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ucs import UCS2

def decode_letter(letter):
	for key, value in UCS2.items():
		if letter == value:
			return key

def decode_msg(message):
	msg, n = '', 4 
	text = [message[i:i+n] for i in range(0, len(message), n)]
	for letter in text:
		msg = msg + decode_letter(letter)
	return msg

