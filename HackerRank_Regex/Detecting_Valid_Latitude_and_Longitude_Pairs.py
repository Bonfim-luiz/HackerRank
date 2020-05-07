# Detecting Valid Latitude and Longitude Pairs
# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem

import re 

regex = r"^\((?:\+|-)?(?:\d(?:\.\d*)?|[0-8][0-9](?:\.\d*)?|90(?:\.0+)?), (?:\+|-)?(?:180(?:\.0+)?|(?:\+|-)?1?[0-7][0-9](?:\.\d*)?|\d\d(?:\.\d*)?)\)$"
n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex, texto)):
    print("Valid")
  else:
    print("Invalid")
