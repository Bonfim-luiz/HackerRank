# Day 4: Geometric Distribution I
# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# Resultado do problema proposto
n = 5
p = 1/3
formula = (1-p)**(n-1)*(p)
print(round(formula,3))

# Automatizando o resultado

n = int(input())
entrada = list(map(int,input().split()))
p = entrada[0]/entrada[1]
formula = (1-p)**(n-1)*(p)
print(round(formula,3))
