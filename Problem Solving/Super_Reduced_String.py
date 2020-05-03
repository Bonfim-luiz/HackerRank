# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

import re
x = True
test_str = input()
while x:
    regex = r"(([a-z])\2)"
    subst = ""
    result = re.sub(regex, subst, test_str)
    if result == test_str:
        x = False
    else:
        test_str = result
if result == "":
    print("Empty String")
else:
    print(result)
