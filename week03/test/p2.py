def drawTriangles(n):
    # 아래쪽 삼각형 출력
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    print()
    # 아래쪽 삼각형 출력
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = 7  # 원하는 크기의 삼각형을 위해 n 값을 변경할 수 있습니다.
drawTriangles(n)