# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

texto = input()
texto = texto.lower()
x = True
alfabeto = 'abcdefghijklmnopqrstuvwxyz '
for i in alfabeto:
    if i in texto:
        pass
    else:
        print('not pangram')
        x = False
        break
if x:
    print('pangram')
