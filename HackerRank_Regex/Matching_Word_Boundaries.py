# Matching Word Boundaries
# https://www.hackerrank.com/challenges/matching-word-boundaries/problem

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
