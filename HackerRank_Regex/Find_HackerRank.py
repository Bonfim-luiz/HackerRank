# Find HackerRank
# https://www.hackerrank.com/challenges/find-hackerrank/problem

import re

n = int(input())
for _ in range(n):
    test_str = input()
    test_str = test_str.lower()
    if bool(re.findall(r"^.+hackerrank$", test_str)):
        print("2")
    elif bool(re.findall(r'^hackerrank.+$', test_str)):
        print("1")
    elif bool(re.findall(r'^hackerrank$', test_str)):
        print("0")
    else:
        print("-1")
