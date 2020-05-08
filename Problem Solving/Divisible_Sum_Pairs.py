# Divisible Sum Pairs
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

from itertools import permutations

def pares(alvo, arr):
    resultado = []
    for subset in permutations(arr, 2):
        if (list(subset)[0] + list(subset)[1]) % alvo == 0:
            resultado.append(list(subset))
    print(int(len(resultado)/2))
    
if __name__ == '__main__':
    n_alvo = list(map(int, input().rstrip().split()))
    alvo = n_alvo[1]
    arr = list(map(int, input().rstrip().split()))
    pares(alvo, arr)
