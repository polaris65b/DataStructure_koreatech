from Functions import *
from Complex import *

class Lab01Test:
    # def test_functions(self):
    #     print("Factorial of 5:", Functions.getFactorial(5))
    #     print("Triangles:")
    #     Functions.drawTriangles(5)
    #     print("Pythagorean triples:")
    #     print(Functions.getTriples(50))

    def test_complex(self):
        complex1 = Complex(1, 2)
        complex2 = Complex(3, 4)
        print("Complex addition:", complex1.add(complex2))
        print("Complex subtraction:", complex1.subtract(complex2))
        print("Complex multiplication:", complex1.multiply(complex2))

    def useComplex():
        z1 = Complex(1.5, 5.6)
        z2 = Complex(4.0, 3.7)
        print(z1)
        print(z2)
        z3 = z1 + z2
        print(z3)
        

    def test_point3d(self):
        point1 = Point3D(1, 2, 3)
        point2 = Point3D(4, 5, 6)
        print("Point1:", point1)
        print("Point1 length:", point1.length())
        print("Distance between Point1 and Point2:", Point3D.distance(point1, point2))
        point1.translate(1, 1, 1)
        print("Translated Point1:", point1)

if __name__ == "__main__":
    test = Lab01Test()
    print("Functions Test:")
    test.test_functions()
    print("\nComplex Test:")
    test.test_complex()
    print("\nPoint3D Test:")
    test.test_point3d()