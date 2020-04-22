# Day 16: Exceptions - String to Integer
# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

#!/bin/python3

import sys

S = input().strip()
entrada = S
try:
    x = int(entrada)
    print(x)
except:
    print("Bad String")