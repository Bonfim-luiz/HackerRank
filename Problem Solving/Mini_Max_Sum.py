# Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem

from itertools import permutations

def miniMaxSum(arr):
    somas = []
    for subset in permutations(arr, 4):
        somas.append(sum(list(subset)))
    print(min(somas), max(somas))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
