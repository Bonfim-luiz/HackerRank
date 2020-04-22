# Matching Digits & Non-Digit Characters
# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem
Regex_Pattern = r"\d\d\D\d\d\D\d{4,}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())