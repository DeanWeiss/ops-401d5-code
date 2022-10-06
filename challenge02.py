#!/bin/python3

# Script: Ops 401d5 Challenge 02
# Author: Dean Weiss
# Date of Last Revision: 4 Oct 2022
# Purpose: Write a Python Script that pings ever 2 seconds and puts response into variable

# Importing from library
import datetime
import time
import os

# Variable of Host IP
hostip = "192.168.0.8"
# variable for pinging the host IP
pingip = (os.system("ping -c 1 " + hostip))
# now is a variable for the datetime command
now = datetime.datetime.now()

# Create Infinite Loop
while True:
    if pingip == 0:
        connection = "Is Up."
    else:
        connection ="Is Down."

    # printing to the screen
    print("Current date and time: ")
    # print string calling the now variable
    print(str(now), connection, hostip)

    # Printing the start time 
    print("Start : %s" % time.ctime())
    print ("End : %s" % time.ctime())

    # 2 Seconds between Pings
    time.sleep(2)

    

# I went here: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
# followed some of the code to get it to print out the response.

# Below here is the code from class, following along as Marco was typing.
# now = datetime.dateime.now()
# print("Current date and time: ")
# print(str(now))

# print("Start : %s" % time.ctime())
# time.sleep(5)
# print ("End : %s" % time.ctime())

# #infinite loop
# # while True: 
# #     print("Start: %s" time.ctime())
# #     time.sleep(5)
# #     print("End : %s" % time.ctime())

# print(os.system("ping 8.8.8.8"))
