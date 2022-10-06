#!/bin/python3

# Script: Ops 401d5 Challenge 03
# Author: Dean Weiss
# Date of Last Revision: 5 Oct 2022
# Purpose: Write a Python Script that pings ever 2 seconds and puts response into variable and then emails the user with updates.

# Importing from library
import datetime
import time
import os
import smtplib

# Input IP
# hostip = input("Enter IP Address") 

# Variable for Host IP
hostip = "192.168.0.8"
# variable for pinging the host IP
pingip = (os.system("ping -c 1 " + hostip))
# now is a variable for the datetime command
now = datetime.datetime.now()

# Enter email and password
# user_email = input("Enter email address")
# password = input("Enter your password")

# User email and password
user_email = "dw.burner21@gmail.com"
password = "vwbrlrcskwjqwsjy"
# Last Status
# last = "blank"
# Ping Result
# ping_result = 1
# Which SMTP server to talk to.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
# login to smtp server
server.login(user_email, password)

# Declaring Function - Pinging the hostip
def IPstatus():
    if pingip == 0:
        last = "Is Up."
    else:
        last ="Is Down."
    return last

# Declaring Function - Email Status Change
def emailStatus():
    IPstatus()
    if pingip != 0:
        change = "Is now down."
    elif pingip == 0:
        change = "Is now up."
    else:
        # send the message
        msg = ("Hello, your connection " + change)
        server.sendmail('mailbot@myserver', user_email, msg)
        server.quit()

# Create Infinite Loop
while True:
    # Putting function as a variable
    connection = IPstatus
     # Calling the emailStatus function
    emailStatus()
    # printing to the screen
    print("Current date and time: ")
    # print string calling the now variable
    print(str(now), connection, hostip)

    # Printing the start and end time of ping 
    print("Start : %s" % time.ctime())
    print ("End : %s" % time.ctime())

    # 2 Seconds between Pings
    time.sleep(2)

# Class Follow Along with Marco

# Which SMTP server to talk to.
# server = smtplib.SMTP_SSL(smtp.gmail.com, 465)
# server.ehlo()

# login to smtp server
# server.login(user_email, password)

# send the message
# msg = "Hello World!"
# server.sendmail('mailbot@myserver', user_email, 'message')
# server.quit()
# App email: dw.burner21@gmail.com
# App Password: vwbrlrcskwjqwsjy