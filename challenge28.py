#!/bin/env python3

# Script: Ops 401d5 Challenge 28
# Author: Dean Weiss
# Date of Last Revision: 09 November 2022
# Purpose: Using Handlers

from scapy.all import sr1, sr, IP, ICMP, TCP
import time
import logging
import logging.config
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


# Create Handler
s_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
s_handler.setlevel(logging.WARNING)
f_handler.SetLevel(logging.ERROR)

# Create and Set Format
s_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
s_handler.setFormatter(s_format)
f_handler.setFormatter(f_format)

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
    logger.addHandler(s_handler)
    logger.addhandler(f_handler)
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