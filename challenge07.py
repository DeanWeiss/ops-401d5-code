#!/bin/python3

# Script: Ops 401d5 Challenge 07
# Author: Dean Weiss
# Date of Last Revision: 11 Oct 2022
# Purpose: File Encryption Script Part 2 of 3

# Importing
from cryptography.fernet import Fernet
import os
import os.path
import sys

# Start

# Menu to prompt the user to select a mode.
def menu():
    option = input("""
                    1: Encrypt a File
                    2: Decrypt a File
                    3: Encrypt a Message
                    4: Decrypt a Message
                    5. Encrypt a Directory
                    6. Decrypt a Directory
                    7. Write New Key
                    8. Exit
                    
                    Please Enter Your Choice: """)
    if option == '1':
        filepath = input("File to be Encrypted: ")
        encrypt_file(filepath)
        
    elif option == '2':
        filepath = input("File to be Decrypted: ")
        decrypt_file(filepath)

    elif option == '3':
        message = input("Message to be Encrypted: ")
        encrypt_message(message.encode())

    elif option == '4':
        message = input("Message to be Decrypted: ")
        decrypt_message(message.encode())
    
    elif option == '5':
        dirpath = input("Path to be Encrypted: ")
        dir_encrypt(dirpath)

    elif option == '6':
        dirpath = input("Path to be Decrypted: ")
        dir_decrypt(dirpath)
    
    elif option == '7':
        write_key()

    elif option == '8':
        sys.exit()

    else: print ("Please select a number 1 thru 8.")


# Function to Generate Key
def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)

# Function to Load Key
def load_key():
    return open("key.key", "rb").read()

# Encrypt a File
def encrypt_file(filepath):
    key = load_key()
    fkey = Fernet(key)
    with open(filepath, 'rb') as f:
        contents = f.read()
        print(contents)
        f.close()
    encrypted = fkey.encrypt(contents)
    with open(filepath, 'wb') as f:
        f.write(encrypted)
        f.close()
    print("Ciphertext is " +str(encrypted.decode('utf-8')))

# Decrypt a File
def decrypt_file(filepath):
    key = load_key()
    fkey = Fernet(key)
    with open(filepath, 'rb') as f:
        contents = f.read()
        print(contents)
        f.close()
    decrypted = fkey.decrypt(contents)
    with open(filepath, 'wb') as f:
        f.write(decrypted)
        f.close()
    print("Decrypted message " + str(decrypted.decode('utf-8')))

# Encrypt the Message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print("Ciphertext is " +str(encrypted.decode('utf-8')))

# Decrypt the Message
def decrypt_message(message):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(message)
    print("Decrypted message " + str(decrypted.decode('utf-8')))

# Encrypt a Directory
def dir_encrypt(dir_path):
    for root, dirs, files in os.walk(dir_path):
        print('Directory: {:s}'.format(root))
        for file in files:
            filename = (os.path.join(root, file))
            encrypt_file(filename)

def dir_decrypt(dir_path):
    for root, dirs, files in os.walk(dir_path):
        print('Directory: {:s}'.format(root))
        for file in files:
            filename = (os.path.join(root, file))
            decrypt_file(filename)
    
# Call Menu Function
while True:
    menu()

# End



# Resources
# https://www.teachyourselfpython.com/challenges.php?a=04_Mini_Projects_NEA_Samples_Tutorials&t=02_Netflix_type_Program_NEA_OCR_Task2&s=01_Main_Menu_Start_Screen
# https://www.techgeekbuzz.com/blog/how-to-encrypt-and-decrypt-files-in-python/

# Notes from Class
