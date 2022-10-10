#!/bin/python3

# Script: Ops 401d5 Challenge 06
# Author: Dean Weiss
# Date of Last Revision: 10 Oct 2022
# Purpose: File Encryption Script Part 1 of 3

# Import Fernet
from email import message
from cryptography.fernet import Fernet

# Declare Variables

# Start

# Menu to prompt the user to select a mode.
def menu():
    option = input("""
                    1: Encrypt a File
                    2: Decrypt a File
                    3: Encrypt a Message
                    4: Decrypt a Message
                    
                    Please Enter Your Choice: """)
    if option == '1':
        filepath = input("File to be Encrypted: ")
        
    elif option == '2':
        filepath = input("File to be Decrypted: ")

    elif option == '3':
        message = input("Message to be Encrypted: ")

    elif option == '4':
        message = input("Message to be Decrypted: ")
    
    else: print ("Please select a number 1 thru 4.")

# Function to Generate Key
def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)

# Function to Load Key
def load_key():
    return open("key.key", "rb").read()

# Encrypt a File
def encrypt_file(file):
    
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


# Call Menu Function

menu()

# End



# Resources
# https://www.teachyourselfpython.com/challenges.php?a=04_Mini_Projects_NEA_Samples_Tutorials&t=02_Netflix_type_Program_NEA_OCR_Task2&s=01_Main_Menu_Start_Screen
# https://www.techgeekbuzz.com/blog/how-to-encrypt-and-decrypt-files-in-python/

# Notes from class
# from  cryptography.fernet import Fernet

# #function declaration

#function to generate key
# Def write_key():
# 	Key = Fernet.generate_key()
# 	With open(“key.key”, “wb”) as key_file:
# 		key_file.write(key)
# #function to load key
# def load_key()
# 	Return open(“key.key”, “rb”).read()
# #function call
# write_key()
# #load generated key
# Key = load_key()
# print(“Key is “ + str(key.decode(‘utf-8’)))

# Message = “This is Top Secret!”.encode()
# print(“Plaintext is “ + str(message.decode(‘utf-8’)))

# #Initialize fernet class
# f = fernet(key)

# #encyprt the message
# Encrypted = f.encrypt(message)

# #print encrypted message to screen
# Print (“Ciphertext is “ + str(encrypted.decode(‘urf-8’)))

# # decrypt the message
# Encrypted_test = “Provide the string you want to decrypt: “)
# Decrypted = f.decrypt(encrypted)
# print(“Decrypted message is “ + str(decrypted.decode(‘utf-8’)))
