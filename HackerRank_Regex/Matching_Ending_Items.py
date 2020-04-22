# Matching Ending Items
# https://www.hackerrank.com/challenges/matching-ending-items/problem

Regex_Pattern = r'^[a-zA-Z]*s$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
