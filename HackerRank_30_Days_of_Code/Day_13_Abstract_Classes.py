# Day 13: Abstract Classes
# https://www.hackerrank.com/challenges/30-abstract-classes/problem

class MyBook():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author 
        self.price = price
    @abstractmethod
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", str(self.price))

