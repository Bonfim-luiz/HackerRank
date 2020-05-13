# Day 5: Normal Distribution I
# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

import math
media = 20
desvio = 2

# Questão 1
formula = lambda x: 0.5 * (1 + math.erf((x - media) / (desvio * (2 ** 0.5))))
resultado = formula(19.5)
print(round(resultado,3))

# Questão 2
resultado_2 = formula(22) - formula(20)
print(round(resultado_2,3))
