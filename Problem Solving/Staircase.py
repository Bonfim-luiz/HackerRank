# Staircase
# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    m = 1
    while n > 0:
        print((n-1)*' ' + m*'#')
        m += 1
        n -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
