# HackerRank Tweets
# https://www.hackerrank.com/challenges/hackerrank-tweets/problem

import re

regex = r"hackerrank"
entrada = ''

for _ in range(int(input())):
    entrada += input() + '\n'

matches = re.findall(regex, entrada, re.MULTILINE | re.IGNORECASE)

print(len(matches))
