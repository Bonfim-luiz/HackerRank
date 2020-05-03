# Alien Username
# https://www.hackerrank.com/challenges/alien-username/problem

import re 

regex = r"^[?:(_|\.)]\d+[a-zA-Z]*_?$"
n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex, texto)):
    print("VALID")
  else:
    print("INVALID")
