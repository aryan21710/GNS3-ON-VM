#!/usr/bin/python


import telnetlib as tn
from scapy.all import *

# FOLLOWING ARE LOCAL MODULES.

import connectivity
import telnet_to_rtr

print ('*' * 100)
print ('STATUS OF CONNECTIVITY WITH 192.168.168.1:-')
print (connectivity.chk_connect('192.168.168.1'))
print ('*' * 100)


print ('\n * 2')
print ('*' * 100)
print (' STATUS OF TELNET TO ROUTER 192.168.168.1')
print (telnet_to_rtr.tel_to_rtr('192.168.168.1'))
print ('*' * 100)


