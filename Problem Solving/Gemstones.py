# Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem

from functools import reduce

def compara(x,y):
    resultado = []
    for i in x:
        if i in y:
            resultado.append(i)
    return set(resultado)

n = int(input())
arr = []
for _ in range(n):
    arr_item = input()
    arr.append(arr_item)

print(len(reduce(compara,arr)))
