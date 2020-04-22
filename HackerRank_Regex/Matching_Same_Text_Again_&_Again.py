# Matching Same Text Again & Again
# https://www.hackerrank.com/challenges/matching-same-text-again-again/problem

Regex_Pattern = r"^((?:[a-z])(?:\w)(?:\s)(?:[^\w])(?:\d)(?:[^\d])(?:[A-Z])(?:[a-zA-Z])(?:[aeiouAEIOU])(?:[^\s]))\1"    

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
