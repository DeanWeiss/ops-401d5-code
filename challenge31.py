#!/bin/env python3

# Script: Ops 401d5 Challenge 31
# Author: Dean Weiss
# Date of Last Revision: 14 November 2022
# Purpose: File Detection

# Libraries
from sys import platform
import os, time


# Declare Functions
# Linux Search
def linuxSearch():
# Ask user for path
    dir = ("Enter directory path.")
# Ask user for a filename
    file = ("Enter name of file.")
# Count number of files searched, store that in a variable
    os.listdir(dir)
# Count the number of files found, store that in a variable

# Print the variables


# Windows Search
def windowsSearch():
# Ask user for path
    dir = ("Enter directory path.")
# Ask user for a filename
    file = ("Enter name of file.")
# Count number of files searched, store tha tin a variable

# Count the number of files found, store that in a variable

# Print the variables



# Determines oS and run appropriate function
if platform == 'linux' or 'platform'== 'linux2':
    print("This is a linux maching")
    linuxSearch()
elif platform == 'win32':
    print("This is a windows maching")
    windowsSearch()