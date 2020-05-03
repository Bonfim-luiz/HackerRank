# Simple Array Sum
# https://www.hackerrank.com/challenges/simple-array-sum/problem

import os
import sys
from functools import reduce

def simpleArraySum(ar):
    return reduce(lambda x,y: x+y,ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
