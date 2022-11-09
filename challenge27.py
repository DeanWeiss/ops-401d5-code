#!/bin/env python3

# Script: Ops 401d5 Challenge 26
# Author: Dean Weiss
# Date of Last Revision: 07 November 2022
# Purpose: Rotating File Handler

import random
from sys import flags
from scapy.all import sr1, sr, IP, ICMP, TCP
import time
import logging
from logging.handlers import RotatingFileHandler

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

def create_rotating_log(path):
    """Creates a Rotating Log"""
    logger = logging.getlogger("Rotating Log")
    logger.setLevel(logging.info)

# seet log rotation and determine format
    handler = RotatingFileHandler (path, maxBytes=20, backupCount=5)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
# set the handler and format to be used
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    print('Logging Started')

    for i in range(100):
        logmsg = "Warning Message"
        logmsg += str(i)
        logger.warning(logmsg)
        logger.info("This is a test log line %s" % i)
        logger.critical("Critical Issue")
        logger.error("An error has occured")
        time.sleep(1.5)

if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)

