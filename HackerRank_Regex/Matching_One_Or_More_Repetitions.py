# Matching One Or More Repetitions
# https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
