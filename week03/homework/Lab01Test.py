# 함수 모듈을 임포트합니다.
from Functions import Functions, Complex, Point3D

# useFunctions() 함수를 사용합니다.
def useFunctions():
    print("1. useFunctions()")
    f1 = Functions()
    n = int(input("getFactorial(n) : "))
    print(f"n의 팩토리얼은 {f1.getFactorial(n)}")
    n2 = int(input("drawTriangles(n2) : "))
    f1.drawTriangles(n2)
    bound = int(input("getTriples(bound) : "))
    f1.getTriples(bound)

# useComplex() 함수를 사용합니다.
def useComplex():
    print("\n\n2. useComplex()")
    z1,z2  = Complex(1.5, 5.6), Complex(4.0, 3.7)
    print(f"z1 : {z1}")
    print(f"z2 : {z2}")
    print(f"z1.실수, z1.허수 : {z1.re}, {z1.im}")
    print(f"z2.실수, z2.허수 : {z2.re}, {z2.im}")
    z3 = z1+z2
    print(f"z1 + z2 = z3 => {z1}+{z2}={z3}")
    z3 = z1-z2
    print(f"z1 - z2 = z3 => {z1}-{z2}={z3}")
    print(f"z3의 절댓값 : {z3.__abs__()}")
    print(f"z3의 문자열 표현 : {z3.__str__()}")
    print(f"z1 * z2 : {z1.__mul__(z2)}")

# usePoint3D() 함수를 사용합니다.
def usePoint3D():
    print("\n3. usePoint()")
    p = Point3D()
    p.__init__(1,2,3)
    print(f"p의 문자열 표현 : {p.__str__()}")
    print(f"p의 표현식 : {p.__repr__()}")
    p1 = Point3D()
    p2 = Point3D(3.6, 2.3, 1.2)
    print(f"p1 : {p1}")
    print(f"p2 : {p2}")
    p1.setCord(4.6, 6.7, 9.0)
    print(f"\np1 = {p1}")
    print(f"p1의 길이 : {p1.length()}")
    print(f"p1과 p2의 거리 : {p1.distance(p2)}")
    x, y, z = map(float, input("translate(x, y, z) like '1.1 2.2 3.3' ").split())
    print(f"p1 translate({x}, {y}, {z}) = {p1.translate(x, y, z)}")

# main() 함수를 사용하여 각 함수를 호출합니다.
def main():
    useFunctions()
    useComplex()
    usePoint3D()

if __name__ == "__main__":
    main()