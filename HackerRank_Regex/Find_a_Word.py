# Find a Word
# https://www.hackerrank.com/challenges/find-a-word/problem

import re

n = int(input())
texto = ' '.join(input() for _ in range(n))

m = int(input())
for _ in range(m):
    regex = r'((?<=\W)|^)%s((?=\W)|$)' % input()
    print(len(re.findall(regex, texto)))
