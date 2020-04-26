# Day 8: Dictionaries and Maps
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Dicionario
n = int(input())
dicionario = {}
for i in range(n):
    cadastro = input()
    cadastro = cadastro.split()
    dicionario[cadastro[0]] = cadastro[1]
while True:
    try:
        busca = input()
        resultado = dicionario.get(busca, 'Not found')
        if resultado == 'Not found':
            print('Not found')
        else:
            print(busca + "=" + resultado)
    except:
        break
