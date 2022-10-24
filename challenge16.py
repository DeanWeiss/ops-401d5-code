#!/bin/env python3

# Script: Ops 401d5 Challenge 16
# Author: Dean Weiss
# Date of Last Revision: 24 Oct 2022
# Purpose: 
# Improt Libraries
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

    # Ask the user for input in the form of a password or string
    # Ask the user for the file path
    # Iterate over each word in the wordlist
    # Check if the user provided password is in the wordlist
    # Print out a message saying the password was found in the wordlist
        # Look into enumerator and readline vs readlines

# Calling the menu function
menu()