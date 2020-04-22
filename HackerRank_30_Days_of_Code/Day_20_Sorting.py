# Day 20: Sorting
# https://www.hackerrank.com/challenges/30-sorting/problem

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
lista = a
swaps = 0
fim = len(lista)
for i in range(fim-1,0,-1):
    for j in range(i):
        if lista [j] > lista [j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            swaps += 1
            
print("Array is sorted in", swaps, "swaps.")
print("First Element:", lista[0])
print("Last Element:", lista[-1])