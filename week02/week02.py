from datetime import date

class Point:
    def __init__(self, x1=0, y1=0):
        self.x = x1
        self.y = y1

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @staticmethod
    def distance(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def translate(self, a, b):
        self.x += a
        self.y += b

class Person:
    def __init__(self, name=' ', age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return '({}, {})'.format(self.name, self.age)

    def __repr__(self):
        return '({}, {})'.format(self.name, self.age)

    @staticmethod
    def isAdult(age):
        return age > 18

    @classmethod
    def fromYear(cls, name, year):
        return cls(name, date.today().year - year)

class Circle:
    def __init__(self, r=1):
        self.r = r

    def __str__(self):
        return 'Circle({})'.format(self.r)

    def getArea(self):
        return 3.14159265358979323846 * self.r ** 2

class Cylinder(Circle):
    def __init__(self, r=1, h=1):
        super().__init__(r)
        self.h = h

    def __str__(self):
        return 'Cylinder({}, {})'.format(self.r, self.h)

    def getVolume(self):
        return self.getArea() * self.h