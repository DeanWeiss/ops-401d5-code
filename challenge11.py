#!/bin/env python3

# Script: Ops 401d5 Challenge 11
# Author: Dean Weiss
# Date of Last Revision: 20 Oct 2022
# Purpose: TCP Port Range Scanner that tests whether a TCP port is open or closed. Part 1 of 3
# Importing Libraries
import random
from sys import flags
from scapy.all import sr1, sr, IP, ICMP, TCP

host = "192.168.0.130" 
# sport, scan port range...yeah, sport
sport = (20, 21, 22, 80)
src_port = 22
for port in sport:
    response=sr1(IP(dst=host)/TCP(sport=src_port,dport=port,flags="S"),timeout=1,verbose=0,) 

    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
        print(str(sport) +": Port is open")
    if response is not None and response.haslayer(TCP) and response.getlayer(TCP).flags==0x14:
        print(str(sport) +": Port is closed")
    else:
        print(str(port) +" Port is filtered and silently dropped")



# Source: I had a real hard time with labs 11-13 and Zack helped me and shared with me his source. https://thepacketgeek.com/scapy/building-network-tools/part-10/