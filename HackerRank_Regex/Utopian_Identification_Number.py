# Utopian Identification Number
# https://www.hackerrank.com/challenges/utopian-identification-number/problem

import re 

regex = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'

n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex, texto)):
    print("VALID")
  else:
    print("INVALID")
