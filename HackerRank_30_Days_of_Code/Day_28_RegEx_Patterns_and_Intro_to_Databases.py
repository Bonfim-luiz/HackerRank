# Day 28: RegEx, Patterns, and Intro to Databases
# https://www.hackerrank.com/challenges/30-regex-patterns/problem
import re
resultado = []
if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if bool(re.match(r"^.+@gmail\.com$", emailID)):
            resultado.append(firstName)
    
    resultado = sorted(resultado)
    
    for i in resultado:
        print(i)