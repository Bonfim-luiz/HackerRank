# Day 5: Loops
# https://www.hackerrank.com/challenges/30-loops/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print("{a} x {b} = {c}".format(a = n, b = i, c = n*i))
