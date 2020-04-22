# Find A Sub-Word
# https://www.hackerrank.com/challenges/find-substring/problem

import re

n = int(input())
texto = "\n".join(input() for _ in range(n))
for j in range(int(input())):
    busca = input()
    Regex = r'(?:[a-zA-Z0-9_])' + busca + '(?:[a-zA-Z0-9_])'
    match = re.findall(Regex, texto)
    print(len(match))
