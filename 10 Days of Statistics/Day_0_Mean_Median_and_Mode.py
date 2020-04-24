# Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import numpy as np
from scipy import stats

n = int(input())
lista = list(map(int, input().split()))
print(np.mean(lista))
print(np.median(lista))
print(int(stats.mode(lista)[0]))
