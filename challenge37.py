#!/bin/env python3

# Script: Ops 401d5 Challenge 36
# Author: Dean Weiss
# Date of Last Revision: 22 November 2022
# Purpose: Web Application Fingerprinting Part 2 of 3

import requests

targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

httpresponse = requests.get(targetsite)
print("HTTP Response")
print(httpresponse)

with open("httpresp.html", "w", encoding='utf-8') as file:
    file.write(str(httpresponse))

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
#
# Stretch Goal
# - Give Cookie Monster hands

# Source: https://stackoverflow.com/questions/40529848/how-to-write-the-output-to-html-file-with-python-beautifulsoup