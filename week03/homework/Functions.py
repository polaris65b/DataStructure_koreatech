import sys, math
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

class Functions:
    # 1 - 1
    def getFactorial(self, n):
        _list = [0 for _ in range(n+1)]
        _list[1] = 1
        for i in range(2, n+1):
            _list[i] = _list[i-1] * i
        return _list[n]
    # 1 - 2
    def drawTriangles(self, lines):
        for i in range(lines - 1, -1, -1):
            print(" " * (lines - i - 1) + "*" * (2 * i + 1))
        print()
        for i in range(lines):
            print(" " * (lines - i - 1) + "*" * (2 * i + 1))
    # 1 - 3
    def getTriples(self, bound):
        n = 1
        print(f"Triples within {bound}")
        for a in range(1, bound):
            for b in range(1, bound):
                for c in range(1, bound):
                    if (a <= b ) and a ** 2 + b ** 2 == c ** 2:
                        print(f"\n{n}) a = {a}, b = {b}, c = {c}")
                        n+=1

#2
class Complex:
    def __init__(self, x = 1, y = 1):
        self.re = x
        self.im = y

    def __repr__(self):
        return f"(re={self.re}, im={self.im}i)"
    def __add__(self, other):
        x, y = self.re+other.re, self.im + other.im
        return Complex(x, y)
    def __sub__(self, other):
        x, y = self.re - other.re, self.im - other.im
        return Complex(x, y)
    def __mul__(self, other):
        x, y = self.re * other.re - self.im * other.im, self.re * other.re + self.im * other.im
        return Complex(x, y)
    def __abs__(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)
    def __str__(self):
        return f"({self.re}, {self.im}i)"
#3
class Point3D:
    def __init__(self, x=0.0,y=0.0,z=0.0 ):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        self.x = abs(self.x)
        self.y = abs(self.y)
        self.z = abs(self.z)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def setCord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f"\n{self.__class__.__name__ } setCord({x},{y},{z})")

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def distance(self, p):
        d1, d2, d3 = (self.x-p.x)**2, (self.y-p.y) ** 2, (self.z-p.z) ** 2
        return math.sqrt(d1+ d2 +d3)
    def translate(self, a,b,c):
        self.x, self.y, self.z = self.x+a, self.y+b, self.z+c
        return self