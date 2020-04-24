# Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

import statistics

n = input()
lista_valores = list(map(int,input().split()))
lista_freq = list(map(int,input().split()))
lista_resultante = []

for i in range(int(n)):
  j = lista_freq[i]
  while j > 0:
    x = lista_valores[i]
    lista_resultante.append(x)
    j = j -1

lista_resultante = sorted(lista_resultante)

q1 = int(statistics.median(lista_resultante[:(len(lista_resultante))//2]))
q2 = int(statistics.median(lista_resultante))
q3 = int(statistics.median(lista_resultante[(len(lista_resultante)+1)//2:]))

print('%.1f'%(q3-q1))
