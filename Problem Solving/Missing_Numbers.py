# Missing Numbers
# https://www.hackerrank.com/challenges/missing-numbers/problem

import os
import collections

def missingNumbers(arr, brr):
    a = collections.Counter(arr)
    b = collections.Counter(brr)
    return sorted((b - a).keys())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = map(int, input().rstrip().split())

    m = int(input())

    brr = map(int, input().rstrip().split())

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
