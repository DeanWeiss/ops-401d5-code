#!/bin/env python3

# Script: Ops 401d5 Challenge 16
# Author: Dean Weiss
# Date of Last Revision: 26 Oct 2022
# Purpose: Brute Force 3 of 3
# Improt Libraries
from pexpect import pxssh
import os
import time
import getpass
import sys

# Menu
def menu():
    option = input("""
                    1: Mode 1: Offensive; Dictionary Iterator
                    2: Mode 2: Defensive; Password Recognized
                    3: Exit
                    
                    Please Enter Your Choice: """)
    if option == '1':
        iterator()
        
    elif option == '2':
        password_check()

    elif option == '3':
        sys.exit()

    else: print ("Please select a number 1 thru 3.")

# Declare Functions

def iterator():
    path = input("Enter your dictionary filepath:\n")
    file = open(path)
    line = file.readline()
    print (line)

    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

def password_check():
    password = getpass("Enter Password.")
    filepath = input("Enter filepath")
    file = open(filepath)
    line = file.readlines()

    while line:
        line = line.rstrip()
        if password == line:
            print ("Your Passsword was found.")
        else:
            print ("No Matching Password.")
    file.close()


session = pxssh.pxssh()
host = input("Please provide an IP address:")
username = input("Please provide a username:")
pwd = getpass.getpass(prompt = "Enter a Password:")

try:
    session.login(host, username, pwd)
    session.sendline('uptime')
    session.prompt()
    print(session.before)
    session.sendline('whoami')
    session.prompt()
    print(session.before)
    session.sendline('ls-l')
    session.prompt()
    print(session.before)
    session.logout()

except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)

# Calling the menu function
menu()