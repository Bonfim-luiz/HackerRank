# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    alice = []
    bob = []
    k = 0
    while k < len(a): 
        if a[k] > b[k]:
            alice.append('x')
        if b[k] > a[k]:
            bob.append('x')
        k += 1
    resultado = [len(alice), len(bob)]
    return(resultado)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
