# Alternative Matching
# https://www.hackerrank.com/challenges/alternative-matching/problem

Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
