# Excluding Specific Characters
# https://www.hackerrank.com/challenges/excluding-specific-characters/problem
Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\r\n\t\f\s][^AEIOU][^\.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
