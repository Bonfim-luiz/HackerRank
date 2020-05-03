# Day 7: Arrays
# https://www.hackerrank.com/challenges/30-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    resultado = ""
    tam = len(arr) - 1
    i = 0
    while i <= tam:
        if tam == 0:
            resultado = resultado + str(arr[tam])
            tam = tam - 1
        else:
            resultado = resultado + str(arr[tam]) + " "
            tam = tam - 1
    print(resultado)
