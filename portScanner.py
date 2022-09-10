# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:21:34 2022

@author: USER
"""

import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.settimeout(5)
#AF_INET: IPV4
#SOCK_STREAM: TCP connect, SOCK_DGRAM: UDP connect

host = input("Please enter the Ip you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

def port_scanner(port):
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")
        
port_scanner(port)