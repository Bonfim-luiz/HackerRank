# Day 26: Nested Logic
# https://www.hackerrank.com/challenges/30-nested-logic/problem

real = input().split()
esperado = input().split()
real = list(map(int,real))
esperado = list(map(int,esperado))

if real[2] > esperado[2]:
    print(10000)
elif real[2] < esperado[2]:
    print("0")
else:
    if real[1] > esperado[1]:
        dif = int(real[1]) - int(esperado[1])
        print(dif*500)
    elif real[1] < esperado[1]:
        print("0")
    else:
        if real[0] != esperado[0] and real[0] > esperado[0]:
            dif = int(real[0]) - int(esperado[0])
            print(dif*15)
        else:
            print("0")