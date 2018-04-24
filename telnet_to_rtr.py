#!/usr/bin/python

import telnetlib as tn
import getpass
from time import sleep

def tel_to_rtr(ip_rtr):
    skt_cont=tn.Telnet(ip_rtr)
    uname='test1'
    print ('PLEASE PROVIDE THE PASSWD FOR USER TEST1 TO LOGIN TO RTR, BE READY \n\n') 
    sleep(5)
    passwd=getpass.getpass()
    print ('LOGIN SCREEN :-',skt_cont) 
    a=skt_cont.read_until("Username: ")
    a1=skt_cont.write(uname+"\n")

    b=skt_cont.read_until("Password: ")
    b1=skt_cont.write(passwd+"\n")
    '''
    print ('a:-',a)
    print ('a1:-',a1)
    print ('b:-',b)
    print ('b1:-',b1)
    '''
    c=skt_cont.read_until("gns3-r1#")
    #print ('c:-',c)
    skt_cont.write("conf t\n")
    skt_cont.write("int lo0\n")
    skt_cont.write("ip address 1.1.1.1 255.255.255.255\n")
    skt_cont.write("no shut\n")
    skt_cont.write("end\n")
    skt_cont.write("show ip interface brief\n")
    skt_cont.write("exit\n")
    print(skt_cont.read_all())
    skt_cont.close()
