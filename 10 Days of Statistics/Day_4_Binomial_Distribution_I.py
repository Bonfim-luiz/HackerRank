# Day 4: Binomial Distribution I
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

def fatorial(n):
    if n < 1:
        return 1
    else:
        return n*fatorial(n-1)
    
def binomial(n,k,p):
    x = fatorial(n)/(fatorial(k)*fatorial(n-k))
    y = (p**k)*((1-p)**(n-k))
    resultado = x * y
    return float("%.3f" % resultado)

resultado_final = 0
for i in range(3,7):
    resultado_final += binomial(6,i,1.09/2.09)
print(resultado_final)   
