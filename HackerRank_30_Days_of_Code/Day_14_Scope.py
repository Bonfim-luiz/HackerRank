# https://www.hackerrank.com/challenges/30-scope/problem
# Day 14: Scope

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()

    def computeDifference(self):
        resultado = []
        for i in self.__elements:
            for j in self.__elements:
                diferenca = i - j
                diferenca = abs(diferenca)
                resultado.append(diferenca)
        return max(resultado)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)