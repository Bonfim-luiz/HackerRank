# Day 6: The Central Limit Theorem I
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

import math

total = 9800
media = 205
qtd = 49
var = 15

Z = (total - (qtd*media))/(var*(math.sqrt(qtd)))
resultado = 0.5*(1 + math.erf(Z/(math.sqrt(2))))
resultado = round(resultado,4)

print(resultado)
