# Day 6: Let's Review
# https://www.hackerrank.com/challenges/30-review-loop/problem

S = int(input())
if 1 <= S and S <= 10:
    for i in range(S):
        word = str(input())
        if 2 <= len(word) and len(word) <= 10000:
            print(word[::2], word[1::2])
