
# Day 4: Geometric Distribution II
# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

# Resultado do problema proposto
n = 5
p = 1/3
resultado = 0
while n > 0:
    formula = (1-p)**(n-1)*(p)
    resultado += formula
    n = n - 1
print(round(resultado,3))

# Automatizando a entrada
n = int(input())
entrada = list(map(int,input().split()))
p = entrada[0]/entrada[1]
resultado = 0
while n > 0:
    formula = (1-p)**(n-1)*(p)
    resultado += formula
    n = n - 1
print(round(resultado,3))
