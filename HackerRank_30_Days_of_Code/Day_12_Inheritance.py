# Day 12: Inheritance
# https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        soma = 0
        for i in self.scores:
            soma += i
        media = soma/len(self.scores)
        if media >= 90 and media <= 100:
            return "O"
        if media >= 80 and media < 90:
            return "E"
        if media >= 70 and media < 80:
            return "A"
        if media >= 55 and media < 70:
            return "P"
        if media >= 40 and media < 55:
            return "D"
        if media < 40:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())