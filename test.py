#!/usr/bin/python
# coding: iso-8859-1

from encode import encode_msg, encode_phn
from send_message import send_message

phone = encode_phn('3704713782')
message = encode_msg('hello world')
send_message(phone,message)

