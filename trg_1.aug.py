x = '10111'

x = x[::-1] #reverse

s = 0
for i in range(len(x)):
    s += int(x[i]) * (2**i)

print(s)
s=0
for i, c in enumerate(x):
    s += int(c) * 2**i
print(s)

i=23
str = ""
while i<0:
    if i%2==0:
        str += "0"
    else:
        str += "1"
    i = i // 2
print("str: ",str[::-1])

'''
trg 17_aug
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_name(self):
        print("My name is:", self.name)

    def print_age(self):
        print("My age is:", self.age)

from math import dist

class Shape:
    def __init__(self, points):
        self.points = points
    def describe(self):
        print("I am a shape")
    def perimiter(self):
        s = 0
        for i in range(len(self.points), 1):
            s += dist(self.points(i),self.points(i+1))
        s+=dist(self.points(-1), self.points(0))
        print("the Perimiter is", s)

class Quadrangle(Shape):
    def __init__(self):
        check this


if __name__ == "__main__":
    p = Person("Moshe", 22)
    p.print_name()
    p.print_age()
