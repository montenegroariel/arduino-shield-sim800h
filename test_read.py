import time
from read_message import read_message
from decode import decode_msg

msg = read_message('46').split('\r\n')
print decode_msg(msg[2])


"""
for x in range(0, 43):
   msg = read_message(str(x)).split('\r\n')
   print decode_msg(msg[2])
   time.sleep(1)
"""	



