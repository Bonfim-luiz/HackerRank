# Day 1: Quartiles
# https://www.hackerrank.com/challenges/s10-quartiles/problem

import statistics

n = int(input())
valores = sorted(map(int,input().split()))

print(int(statistics.median(valores[:n//2])))
print(int(statistics.median(valores)))
print(int(statistics.median(valores[(n+1)//2:])))
