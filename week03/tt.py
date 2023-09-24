from Lab02 import Matrix, EightQueen, TicTacToe

def useMatrix():
    m1 = Matrix(5, 5)#, 'r')
    m1.mPrint()
    m2 = Matrix(5, 5)#, 'r')
    m2.mPrint()
    m = m1 + m2  # '+' 연산자로 두 개의 Matrix 객체를 더합니다.
    m.mPrint()

def useEightQueen():
    q1 = EightQueen()
    q1.print_board()

def useTicTacToe():
    t1 = TicTacToe()
    t1.play_ttt()
    t1.print_board

def main():
    # useMatrix()  # 함수 호출을 수정하여 괄호 ()를 사용합니다.
    # useEightQueen()
    useTicTacToe()

if __name__ == "__main__":
    main()