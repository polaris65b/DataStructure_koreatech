from week02 import Point, Person, Circle, Cylinder

def tstCC():
    c1 = Circle(1)
    s1 = Cylinder(34, 6)
    print(c1)
    print(s1)
    print("Cylinder Volume:", s1.getVolume())

def tstPerson():
    p1 = Person('Tariq', 40)
    p2 = Person('Ali', 2001)
    print(p1)
    print(p2)
    print("Is Ali an adult?", Person.isAdult(p2.age))

def tstPoint():
    p1 = Point()
    p2 = Point(5)
    p3 = Point(5, 8)
    print(p1)
    print(p2)
    print(p3)
    print("Length of p3:", p3.length())
    print("Translated p1:", p1)

def main():
    tstPoint()
    tstPerson()
    tstCC()

if __name__ == "__main__":
    main()