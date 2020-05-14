# Day 5: Normal Distribution II
# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math

media = 70
desvio = 10

formula = lambda x: 0.5 * (1 + math.erf((x - media) / (desvio * (2 ** 0.5))))

maior_80 = round((1 - formula(80))*100,2)
maior_60 = round((1 - formula(60))*100,2)
menor_60 = round((formula(60))*100,2)

print(maior_80)
print(maior_60)
print(menor_60)
