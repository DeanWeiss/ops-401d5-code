#!/bin/env python3

# Script: Ops 401d5 Challenge 32
# Author: Dean Weiss
# Date of Last Revision: 15 November 2022
# Purpose: File Detection 2 of 3

# Libraries
from sys import platform
import os, hashlib


# Declare Functions
# Linux Search
def linuxSearch():
# Ask user for path
    dirpath = ("Enter directory path.")
# Ask user for a filename
    filename = ("Enter name of file.")
# Count number of files searched, store tha tin a variable
    filesearch = 0
    for root, dirs, files in os.walk(dirpath):
        for file in files:
# Count the number of files found, store that in a variable            
            filesearch+=1
            if file==filename:
# Print the variables
                print(str(filesearch)+" your files are " +root+"/"+filename)


# Windows Search
def windowsSearch():
# Ask user for path
    dirpath = ("Enter directory path.")
# Ask user for a filename
    filename = ("Enter name of file.")
# Count number of files searched, store tha tin a variable
    filesearch = 0
    for root, dirs, files in os.walk(dirpath):
        for file in files:
# Count the number of files found, store that in a variable            
            filesearch+=1
            if file==filename:
# Print the variables
                print(str(filesearch)+" your files are " +root+"/"+filename)


# Determines oS and run appropriate function
if platform == 'linux' or 'platform'== 'linux2':
    print("This is a linux maching")
    linuxSearch()
elif platform == 'win32':
    print("This is a windows maching")
    windowsSearch()


# Class Demo
def hash_file(filename):
    # This function returns the SHA-256 hash of the file pass into it

    # Make a hash object
    h = hashlib.sha256()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        # loop till the end of the file
        block = 0
        while block != b'':
            # Read only 1024 bytes a time
            block = file.read(1024)
            h.update(block)
            print(h)

    # return the hex representation of the hash digest
    return h.hexdigest()

# Substitue the file name as the parameter
message = hash_file("challenge32test.txt")
print(message)

# Timestamp Function

# Hash Function

# Has getter function
# use os.walk to crawl through directories and print to the screen all the file hashes

# Menu Options
# 1. Check OS, search for file
# 2. Get File Hashes for all files in a folder
# 3. Profit  .... 

