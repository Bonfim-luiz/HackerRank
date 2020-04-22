# Detect the Email Addresses
# https://www.hackerrank.com/challenges/detect-the-email-addresses/problem

import re

regex = '\w+[.\w]*@\w+[.\w]+\w+'
entrada = ''
for _ in range(int(input())):
    entrada += input() + '\n'

print(';'.join(sorted(set(re.findall(regex,entrada)))))
