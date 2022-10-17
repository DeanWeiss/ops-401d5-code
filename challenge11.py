#!/bin/env python3

# Script: Ops 401d5 Challenge 11
# Author: Dean Weiss
# Date of Last Revision: 17 Oct 2022
# Purpose: TCP Port Range Scanner that tests whether a TCP port is open or closed.
# Importing Libraries
from scapy.all import sr1,IP,ICMP,TCP

# Variables
# IP Address of a Windows VM I booted up.
host = "192.168.0.13"
port_range = [22, 23, 80, 443, 3389]
src_port = [22]
dst_port = [22, 23, 80, 443, 3380]

response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)


# For Loop
for x in port_range:
    response
    if (str(response)) == "0x12":
        print ("Port is Open.")
    elif (str(response)) == "0x14":
        print ("Port is Closed")
    elif (str(response)) == "None":
        print ("Port is filtered and silently dropped")