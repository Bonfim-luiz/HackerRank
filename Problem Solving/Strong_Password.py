# Strong Password
# https://www.hackerrank.com/challenges/strong-password/problem

import re
n = int(input())
texto = input()
resultado = 0
if n < 6:
    tamanho = 6 - n
else:
    tamanho = 0
if bool(re.findall(r'[A-Z]',texto)) == False:
    resultado += 1 
if bool(re.findall(r'[a-z]',texto)) == False:
    resultado += 1
if bool(re.findall(r'[!@#$%^&*()\-+]',texto)) == False:
    resultado += 1
if bool(re.findall(r'\d',texto)) == False:
    resultado += 1
if tamanho > resultado:
    print(tamanho)
else:
    print(resultado)
