# Day 10: Binary Numbers
# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

if __name__ == '__main__':
    n = int(input())
    binario = bin(n)
    binario_str = str(binario[2:])
    lista = []
    for elemento in binario_str:
        x = int(elemento)
        lista.append(x)

    saida = [sum(i) for _, i in groupby(lista)]    
    print(max(saida))