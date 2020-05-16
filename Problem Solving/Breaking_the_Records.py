# Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

def breakingRecords(scores):  
    maximo = 0
    i = 0
    x = scores[0]
    while i < (len(scores) - 1):
        if x < scores[(i + 1)]:
            maximo += 1
            x = scores[(i + 1)]
        i += 1

    minimo = 0
    j = 0
    y = scores[0]
    while j < (len(scores) - 1):
        if y > scores[(j + 1)]:
            minimo += 1
            y = scores[(j + 1)]
        j += 1
    resultado = [maximo, minimo]
    return resultado

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
