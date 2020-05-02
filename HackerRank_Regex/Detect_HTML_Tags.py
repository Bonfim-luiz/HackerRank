# Detect HTML Tags
# https://www.hackerrank.com/challenges/detect-html-tags/problem

import re 

regex = r"(?:<(\w+))"
resultado = []
for i in range(int(input())):
    texto = input()
    x = re.findall(regex, texto)
    for j in x:
        resultado.append(j)

a = sorted(set(resultado))
final = ""
for k in a :
    if k is a[0]:
        final = k
    else:
        final = final + ";" + k
print(final)
