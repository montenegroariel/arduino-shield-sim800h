#!/usr/bin/env python
# -*- coding: latin-1 -*-

from ucs import UCS2
import string


def encode_msg(message):
    msg = ''
    for letter in message:
		msg = msg + UCS2[letter]
    return msg
    
def encode_phn(phone):
    phn = ''
    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)  
    phone_number=phone.translate(all, nodigs)

    for number in phone_number:
       phn = phn + '003' + number
    return phn        

