# Day 0: Weighted Mean
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

n = input()
valores = input()
peso = input()

lista_valores = list(map(int, valores.split()))
lista_peso = list(map(int, peso.split()))
soma = 0
divisor = 0

for i in range(len(lista_valores)):
    soma += lista_valores[i]*lista_peso[i]
for y in lista_peso:
    divisor += y

resultado = round(soma/divisor,1)
print(resultado)
