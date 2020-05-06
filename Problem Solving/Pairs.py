# Pairs
# https://www.hackerrank.com/challenges/pairs/problem

# 3 resoluções com perfomances diferentes

# Menos eficiente
from itertools import permutations

def pares(alvo, arr):
    resultado = []
    for subset in permutations(arr, 2):
        if (list(subset)[0] - list(subset)[1]) == alvo:
            resultado.append(list(subset))
    print(len(resultado))

if __name__ == '__main__':
    n_alvo = list(map(int, input().rstrip().split()))
    alvo = n_alvo[1]
    arr = list(map(int, input().rstrip().split()))
    pares(alvo, arr)
    
# Pouco eficiente
def pares(alvo, arr):
    contador = 0
    for i in arr:         
        soma = i + alvo
        if soma in arr:
            contador += 1
    print(contador)

if __name__ == '__main__':
    n_alvo = list(map(int, input().rstrip().split()))
    alvo = n_alvo[1]
    arr = list(map(int, input().rstrip().split()))
    pares(alvo, arr)
   
# Mais eficiente
def pares(alvo, arr):
    numbers = set()
    count = 0
    for n in arr:
        if n + alvo in numbers:
            count += 1
        if n - alvo in numbers:
            count += 1
        numbers.add(n)
    print(count)

if __name__ == '__main__':
    n_alvo = list(map(int, input().rstrip().split()))
    alvo = n_alvo[1]
    arr = list(map(int, input().rstrip().split()))
    pares(alvo, arr)
