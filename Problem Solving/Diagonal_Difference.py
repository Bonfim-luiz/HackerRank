# Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    j = 0
    k = -1
    diagonal_principal = []
    diagonal_inversa = []
    for i in arr:
        diagonal_principal.append(i[j])
        diagonal_inversa.append(i[k])
        j += 1
        k -= 1
    return(abs(sum(diagonal_principal) - sum(diagonal_inversa)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
