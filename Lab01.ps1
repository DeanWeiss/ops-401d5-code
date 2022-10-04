# Script: Ops 401d5 Lab 01
# Author: Dean Weiss
# Date of Last Revision: 3 Oct 2022
# Purpose: Write a Powershell script that changes screen lock time

#main

powercfg.exe /setacvalueindex scheme_current sub_video videoidle 10
powercfg.exe /setactive scheme_current

#end