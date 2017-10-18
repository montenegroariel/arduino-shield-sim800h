from encode import encode_msg, encode_phn
from send_message import send_message

number = '3704 - 713781 '
phone = number.replace('-','')
phone = phone.replace(' ','')



x='aaa12333bb445bb54b5b52'
import string
all=string.maketrans('','')
nodigs=all.translate(all, string.digits)
a= x.translate(all, nodigs)
print(a)

import urllib2
#urllib2.urlopen('http://10.91.2.56:8009/?3704713781:21')
#phone = number.strip()
#print(phone)


phone = encode_phn('3704713781')
message = encode_msg('a')
send_message(phone,message)
#send_message('+543704713781','a')

