import math

class Functions:
    @staticmethod
    def getFactorial(n):
        if n < 0:
            print("inaccurate input")
            return None
        elif n == 0 or n == 1:
            return 1
        else:
            return n * Functions.getFactorial(n - 1)

    @staticmethod
    def drawTriangles(self, lines):
        # n = 2*lines - 1
        for lines in range(self, lines):
            print(' ' * (line - 1), end = ' ')
            print("*"*(2 * lines + 1 - 2 * line))
        print()
        for line in range(lines + 1):
            print(" " * (line - 1), end = " ")
            print("*", lines + 1 - 2 * line)

    @staticmethod  
    def getTriples(self, bound):
        print("Pythagorean Triples within {}".format(bound))
        for a in range(1, bound):
            for b in range(1, bound):
                for c in range(1, bound):
                    if (a * a + b * b  + c * c):
                        print("{},{},{}".format(a,b,c))

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def setCord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)

    def translate(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"