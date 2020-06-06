# Left Rotation
# https://www.hackerrank.com/challenges/array-left-rotation/problem

# Solução lenta
tamanho_movimentos = input().split()
tamanho = int(tamanho_movimentos[0])
movimentos = int(tamanho_movimentos[1])
lista = list(map(int, input().rstrip().split()))

i = 0
original = lista.copy()
while i < movimentos:
    b = lista.copy()
    j = 0
    while j < len(lista):
        if j == (len(lista) - 1):
            b[j] = lista[0]
        else:
            b[j] = lista[j + 1]
        j += 1
    lista = b.copy()
    i += 1

print(*b, sep = ' ')

# Solução mais rápida
tamanho_movimentos = input().split()
tamanho = int(tamanho_movimentos[0])
movimentos = int(tamanho_movimentos[1])
lista = list(map(int, input().rstrip().split()))

def rotate(lista, x):
    resultado = lista[x:] + lista[:x]
    return resultado

x = movimentos % tamanho
print(*rotate(lista,x), sep = ' ')
