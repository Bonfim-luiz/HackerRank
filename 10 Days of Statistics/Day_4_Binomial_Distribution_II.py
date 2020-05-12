# Day 4: Binomial Distribution II
# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

def fatorial(n):
    if n < 1:
        return 1
    else:
        return n*fatorial(n-1)
    
def binomial(n,k,p):
    x = fatorial(n)/(fatorial(k)*fatorial(n-k))
    y = (p**k)*((1-p)**(n-k))
    resultado = x * y
    return resultado

menos_q_x = 0
for i in range(0,3):
    menos_q_x += binomial(10,i,12/100)
print("%.3f" % menos_q_x)

mais_q_x = 0
for i in range(2,11):
    mais_q_x += binomial(10,i,12/100)
print("%.3f" % mais_q_x)
