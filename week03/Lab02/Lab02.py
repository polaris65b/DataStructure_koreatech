import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[random.random() for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join([str(round(x, 2)) for x in row]) + "\n"
        return matrix_str

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("두 행렬의 크기가 일치하지 않아 더할 수 없습니다.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("첫 번째 행렬의 열 수와 두 번째 행렬의 행 수가 일치하지 않아 곱셈을 수행할 수 없습니다.")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                result.data[i][j] = dot_product
        return result

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

class EightQueens:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]  # 8x8 체스 보드 초기화
        self.place_queens()

    def place_queens(self):
        for row in range(8):
            col = random.randint(0, 7)  # 해당 행에 퀸을 랜덤하게 배치
            self.board[row][col] = 1

    def is_safe(self, row, col):
        # 같은 열에 다른 퀸이 있는지 확인
        for i in range(8):
            if self.board[i][col] == 1:
                return False
        
        # 왼쪽 위 대각선 방향에 다른 퀸이 있는지 확인
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        # 오른쪽 위 대각선 방향에 다른 퀸이 있는지 확인
        for i, j in zip(range(row, -1, -1), range(col, 8)):
            if self.board[i][j] == 1:
                return False
        
        return True

    def solve(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == 1 and not self.is_safe(row, col):
                    # 현재 위치에 퀸이 있지만 안전하지 않으면 다시 배치
                    self.board[row][col] = 0
                    self.place_queens()
                    return True  # 퀸 재배치 후 다시 확인
        return True  # 모든 퀸이 안전하게 배치됨

    def print_board(self):
        for row in self.board:
            print(" ".join(["Q" if x == 1 else "." for x in row]))

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 게임 보드 초기화
        self.current_player = "X"  # 현재 플레이어 (X 또는 O)
        self.winner = None  # 게임의 승자 (X, O, 또는 무승부)

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == " " and not self.winner:
            self.board[row][col] = self.current_player
            self.check_winner()
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

    def check_winner(self):
        # 가로, 세로, 대각선으로 승자를 확인합니다.
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                self.winner = self.board[i][0]
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                self.winner = self.board[0][i]
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner = self.board[0][2]
            return

    def is_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))