#!/bin/env python3

# Script: Ops 401d5 Challenge 26
# Author: Dean Weiss
# Date of Last Revision: 07 November 2022
# Purpose: Event Logging

import logging
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
# Not to log events into root, log events into a bucket.
log = logging.getLogger(__name__)

while True:
    # Logging Implementation
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info('Start Session')
    port()
    logging.info('End Session')