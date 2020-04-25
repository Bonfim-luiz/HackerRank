# Day 5: Poisson Distribution I
# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# Solução
import math
k = 5
alpha = 2.5 
formula = round(((math.exp(-alpha))*(alpha**k))/math.factorial(k),3)
print(formula)

# Automatizando as entradas
import math
k = int(input())
alpha = int(input()) 
formula = round(((math.exp(-alpha))*(alpha**k))/math.factorial(k),3)
print(formula)
