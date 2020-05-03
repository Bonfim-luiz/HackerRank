# Plus Minus
# https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

def plusMinus(arr):
    positivos = []
    negativos = []
    zeros = []
    for i in arr:
        if i > 0:
            positivos.append(i)
        elif i < 0:
            negativos.append(i)
        else:
            zeros.append(i)

    print('%.6f' %((len(positivos)/len(arr))))
    print('%.6f' %((len(negativos)/len(arr))))
    print('%.6f' %((len(zeros)/len(arr))))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
