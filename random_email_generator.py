#!/usr/bin/env python3

import random
import sys
import os

randnums = ''

i = 0
while i < int(sys.argv[1]):
    randnum = random.randint(0,9)
    randnums += str(randnum)
    i += 1

user = os.environ['USER']

# Set default to gmail if no domain is selected
# domain = 'gmail.com'

if len(sys.argv) == 2:
    domain = 'gmail'
elif len(sys.argv) == 3:
    if sys.argv[2] == 'g':
        domain = 'gmail'
    elif sys.argv[2] == 'o':
        domain = 'outlook'
    elif sys.argv[2] == 'y':
        domain = 'yahoo'
    elif sys.argv[2] == 'p':
        domain = 'protonmail'
    elif sys.argv[2] == 't':
        domain = 'tutanota'
    else:
        print(f"{sys.argv[1]} is not a recognisable domain!")
        exit()

email = f"{user}{randnums}@{domain}.com\n"
random_email_file = os.path.join(os.environ['HOME'], 'Documents', 'random-emails.txt')

if os.path.exists(random_email_file):
    with open(random_email_file, 'a') as f:
        f.writelines(email)
else: 
    with open(random_email_file, 'w') as f:
        f.writelines(email)
