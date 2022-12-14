#!/bin/env python3

# Script: Ops 401d5 Challenge 31
# Author: Dean Weiss
# Date of Last Revision: 14 November 2022
# Purpose: File Detection 1 of 3

# Libraries
from sys import platform
import os


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

# os.system("ls " + str(file) + " | echo \"$(wc -l) files searched.\"")