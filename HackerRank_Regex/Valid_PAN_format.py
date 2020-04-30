# Valid PAN format
# https://www.hackerrank.com/challenges/valid-pan-format/problem
 
import re 

regex = r'^[A-Z]{5}\d{4}[A-Z]$'

n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex, texto)):
    print("YES")
  else:
    print("NO")
