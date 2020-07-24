# Arrays - DS
# https://www.hackerrank.com/challenges/arrays-ds/problem

import math
import os
import random
import re
import sys

def reverseArray(x):
    resultado = []
    tam=len(x)
    for i in x:
        resultado.append(x[tam-1])
        tam=tam-1
    return(resultado)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
