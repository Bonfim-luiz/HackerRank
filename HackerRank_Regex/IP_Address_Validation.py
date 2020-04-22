# IP Address Validation
# https://www.hackerrank.com/challenges/ip-address-validation/problem

import re 

regex_IPv4 = r'^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$'
regex_IPv6 = r'^(?:[\da-fA-F]{1,4}:){7}[\da-fA-F]{4}$'

n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex_IPv4, texto)):
    print("IPv4")
  elif bool(re.findall(regex_IPv6, texto)):
    print("IPv6")
  else:
    print("Neither")
