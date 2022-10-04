#!/bin/python3

# Script: Ops 401d5 Challenge 02
# Author: Dean Weiss
# Date of Last Revision: 4 Oct 2022
# Purpose: Write a Python Script that pings ever 2 seconds and puts response into variable

# Importing from library
import datetime
import time
import os

hostip = "8.8.8.8"
response = os.system("ping -c 1 " + hostip)

while True:
    # now is a variable for the datetime command
    now = datetime.datetime.now()
    # printing to the screen
    print("Current date and time: ")
    # print string calling the now variable
    print(str(now))

    # Printing the start time 
    print("Start : %s" % time.ctime())
    print ("End : %s" % time.ctime())
    time.sleep(2)
    print(os.system("ping -c 1 " + hostip))
    if response == 0:
        print (hostip, "Is Up.")
    else:
        print (hostip, "Is Down.")
    

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
