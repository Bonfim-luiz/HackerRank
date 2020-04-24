# Day 1: Standard Deviation
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

import numpy as np

n = input()
lista = input()

lista_valores = list(map(int,lista.split()))
resultado = np.std(lista_valores)

print('%.1f'%(resultado))

# Outra alternativa

n = int(input())
valores = list(map(int,input().split()))

media = sum(valores) / n
variacao = sum([((x - media) ** 2) for x in valores]) / n
desvio = variacao ** 0.5

print("{0:0.1f}".format(desvio))
