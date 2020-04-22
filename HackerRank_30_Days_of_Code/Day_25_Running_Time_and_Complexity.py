# Day 25: Running Time and Complexity
# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
import math

def prime(entrada):
    if entrada == 1:
        return "Not prime"
    raiz = int(math.sqrt(entrada))
    for x in range(2, raiz+1):
        if entrada % x == 0:
            return "Not prime"
    return "Prime"

n = int(input())

for i in range(n):
    k = int(input())
    print(prime(k))