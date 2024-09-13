#!/usr/bin/env python3

import random
import sys

lcl = [chr(i) for i in range(97,123)]
ucl = [chr(i) for i in range(65,91)]
nums = [i for i in range(0,10)]
sc = '!@#$%^&*?-'

chars = ''

for i in lcl:
    chars += i

for i in ucl:
    chars += i

for i in nums:
    chars += str(i)

chars += sc

def generate_password():
    rand_chars = random.choices(chars)
    # with open('pw.txt', 'a') as f:
    for rand_char in rand_chars:
        print(rand_char, end='')
            # f.write(rand_char)

if len(sys.argv) == 1:
    max_chars = int(input('Enter password length: '))
elif len(sys.argv) == 2:
    max_chars = int(sys.argv[1])
else:
    print('You entered too many arguments!')

i = 0
while i < max_chars:
    generate_password()
    i += 1
