#!/bin/env python3

# Script: Ops 401d5 Challenge 32
# Author: Dean Weiss
# Date of Last Revision: 15 November 2022
# Purpose: File Detection 2 of 3

# Libraries
from sys import platform
import os, hashlib


import os, hashlib, time, datetime

def timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m-%d-%y %H:%M:%S:%f")
    return str(timestamp)

def hash_it(datapath):
    md5_hash = hashlib.md5()
    with open(datapath,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        print(md5_hash.hexdigest())
     

def linux():
    filepath = input("Input absolute directory path: \n")
    for root, files in os.walk(filepath):
        for name in files:
            datapath = (os.path.join(root, name))
            time = timestamp()
            print(time)
            hash = hash_it(datapath)
            apikey = os.getenv('API_KEY_VIRUSTOTAL')
             
            query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

os.system(query)
            
    
    
linux()

