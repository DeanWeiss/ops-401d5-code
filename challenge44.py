#!/bin/env python3

# Script: Ops 401d5 Challenge 44
# Author: Dean Weiss
# Date of Last Revision: 5 December 2022
# Purpose: Port Scanner

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = timeout=2# TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input("Enter Host IP Address")# TODO: Collect a host IP from the user.
portno = input("Enter Port Number")# TODO: Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.socket((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)