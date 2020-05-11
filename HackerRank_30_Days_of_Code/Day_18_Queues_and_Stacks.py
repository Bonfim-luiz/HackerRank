# https://www.hackerrank.com/challenges/30-queues-stacks/problem
# Day 18: Queues and Stacks

# Minha solução mais compacta
s = 'racecar'
n = int(len(s)/2)

def teste(s):
    i = -1
    j = 0
    while j < n:
        if s[j] != s[i]:
            return False
        i -= 1
        j += 1
    return True
teste(s)

# Minha resposta conforme solicitado no site
import sys
class Solution:
    def __init__(self):
        self.mystack = list()
        self.myqueue = list()
    def pushCharacter(self, char):
        self.mystack.append(char)
    def popCharacter(self):
        return(self.mystack.pop(-1))
    def enqueueCharacter(self, char):
        self.myqueue.append(char)
    def dequeueCharacter(self):
        return(self.myqueue.pop(0))

s=input()
obj=Solution()   
l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True

for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
