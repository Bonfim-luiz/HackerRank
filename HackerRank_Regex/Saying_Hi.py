# Saying Hi
# https://www.hackerrank.com/challenges/saying-hi/problem

import re 

regex = r'^(?:H|h)(?:I|i)\s[^(?:D|d)].*$'

n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex, texto)):
    print(texto)
