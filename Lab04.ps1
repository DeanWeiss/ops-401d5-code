# Script: Ops 401d5 Lab 04
# Author: Dean Weiss
# Date of Last Revision: 6 Oct 2022
# Purpose: Copy it to your public GitHub repo as a new entry. Link to it in your submission.

# Start

net accounts /minpwlen:14
Set-SmbServerConfiguration -EnableSMB1Protocol $false

# Stop