# Split the Phone Numbers
# https://www.hackerrank.com/challenges/split-number/problem

import re 

regex = r'^(\d+)(?: |\-)(\d+)(?: |\-)(\d+)$'

for i in range(int(input())):
    texto = input()
    x = re.findall(regex, texto)
    CountryCode, LocalAreaCode, Number = x[0]
    print('CountryCode=%s,LocalAreaCode=%s,Number=%s' %(CountryCode, LocalAreaCode, Number))
