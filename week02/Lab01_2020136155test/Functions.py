class Functions:
    @staticmethod
    def getFactorial(n):
        if n < 0:
            print("잘못된 입력")
            return None
        elif n == 0 or n == 1:
            return 1
        else:
            return n * Functions.getFactorial(n - 1)

    @staticmethod
    def drawTriangles(n):
        for i in range(n):
            print(' ' * i + '*' * (2 * (n - i) - 1))
        print()
        for i in range(n):
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    @staticmethod
    def getTriples(limit):
        triples = []
        for side1 in range(1, limit + 1):
            for side2 in range(side1, limit + 1):
                for hypotenuse in range(side2, limit + 1):
                    if side1 ** 2 + side2 ** 2 == hypotenuse ** 2:
                        triples.append((side1, side2, hypotenuse))
        return triples