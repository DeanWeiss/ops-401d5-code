#!/bin/env python3

# Script: Ops 401d5 Challenge 36
# Author: Dean Weiss
# Date of Last Revision: 21 November 2022
# Purpose: Web Application Fingerprinting Part 1 of 3
#import modules
import os
import socket
import time
import subprocess

# User Input
a = input("Type in an URL or Ip address you want to fingerprint")
p = input("Type port you would like to check: ")

def netcat(a, p):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))
    run = "nc" + a + " " + p
    sock.sendall(run.encode())
    res = " "

# Check with a While loop
    while True:
        data = sock.rec(1024)
        if (not data):
            break
        res += data.decod()
    print(res)
    sock.close()

# Telnet function definiation
def telnet():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))
    telnet=("telnet " +  str(a) + ' '+ str(p))
    return os.system(telnet)

# Nmap function
def nmap():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))
    os.system("nmap" + str(a) + str(p))
    return os.system(nmap)

# Calling Functions
netcat()
telnet()
nmap()