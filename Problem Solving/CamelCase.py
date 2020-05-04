# CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem

import os
import re

def camelcase(s):
    regex = r'[A-Z]'
    x = re.findall(regex,s)
    return (len(x)+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
