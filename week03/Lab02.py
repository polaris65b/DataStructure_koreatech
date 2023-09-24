import random

class Matrix:
    rnb = random.Random()

    def __init__(self, rows, cols):
        self.M = []
        for _ in range(rows):
            self.M.append([self.rnb.randint(1, 10) for _ in range(cols)])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.M])

    def __repr__(self):
        return repr(self.M)

    def __add__(self, other):
        if len(self.M) != len(other.M) or len(self.M[0]) != len(other.M[0]):
            raise ValueError("Matrix dimensions do not match for addition.")
        
        result = Matrix(len(self.M), len(self.M[0]))
        for i in range(len(self.M)):
            result.M[i] = [self.M[i][j] + other.M[i][j] for j in range(len(self.M[0]))]
        
        return result

    def __sub__(self, other):
        if len(self.M) != len(other.M) or len(self.M[0]) != len(other.M[0]):
            raise ValueError("Matrix dimensions do not match for subtraction.")
        
        result = Matrix(len(self.M), len(self.M[0]))
        for i in range(len(self.M)):
            result.M[i] = [self.M[i][j] - other.M[i][j] for j in range(len(self.M[0]))]
        
        return result

    def __mul__(self, other):
        if len(self.M[0]) != len(other.M):
            raise ValueError("Matrix dimensions do not match for multiplication.")
        
        result = Matrix(len(self.M), len(other.M[0]))
        for i in range(len(self.M)):
            for j in range(len(other.M[0])):
                result.M[i][j] = sum(self.M[i][k] * other.M[k][j] for k in range(len(self.M[0])))
        
        return result

    def transpose(self):
        result = Matrix(len(self.M[0]), len(self.M))
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                result.M[j][i] = self.M[i][j]
        
        return result

# class Matrix:
#     rnb = random.Random()    
#     def __init__(self, rows, cols, f):
#         self.M = []
#         if f == 'r':
#             self.rMatrix(rows, cols)
#         else:
#             self.zMatrix(rows, cols)

#     def rMatrix(self, rows, cols):
#         while len(self.M) < rows:

#             self.M.append([])
#             while len(self.M[-1]) < cols:
#                 self.M[-1].append(self.rnb.randint(1, 10))

#     def zMatrix(self, rows, cols):
#         while len(self.M) < rows:
#             self.M.append([])
#             while len(self.M[-1]) < cols:
#                 self.M[-1].append(0)

    def mPrint(self):
        for row in self.M:
            print(row)

#     def __str__(self):
#         return '\n'.join([' '.join(map(str, row)) for row in self.M])

#     def __repr__(self):
#         return self.__str__()
    
#     def __add__(self, other):
#         rowsA=len(self.M)
#         colsA=len(self.M[0])
#         C=Matrix(rowsA, colsA, 'z')
#         for row in range(rowsA):
#             for col in range(colsA):
#                 C.M[row][col] = self.M[row][col ] + other.M[row][col]
        
#         return C
#     def __sub__(self, other):
#         pass
#     def __mul__(self):
#         pass
#     def __transpose(self):
#         pass

class EightQueen:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.place_queens()

    def is_safe(self, row, col):
        # 같은 열에 퀸이 있는지 확인
        for i in range(8):
            if self.board[i][col] == 1:
                return False
        
        # 왼쪽 위 방향 대각선에 퀸이 있는지 확인
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # 오른쪽 위 방향 대각선에 퀸이 있는지 확인
        for i, j in zip(range(row, -1, -1), range(col, 8)):
            if self.board[i][j] == 1:
                return False
        
        return True

    def place_queens(self):
        for col in range(8):
            row = random.randint(0, 7)
            while not self.is_safe(row, col):
                row = random.randint(0, 7)
            self.board[row][col] = 1

    def print_board(self):
        for row in self.board:
            print(" ".join(["Q" if x == 1 else "." for x in row]))

class TicTacToe:
    def __init__(self):
        self.board = [-1] * 9  # 초기 게임 보드 (9칸)

    def play_ttt(self):
        turn = 0
        while True:
            self.print_board()
            if turn % 2 == 0:
                player = "X"
            else:
                player = "O"
            
            position = self.get_input(player)
            if self.board[position] == -1:
                self.board[position] = player
                if self.check_win(player):
                    self.print_board()
                    print(f"Player {player} wins!")
                    break
                turn += 1
            else:
                print("Invalid move. Try again.")

    def get_input(self, player):
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (0-8): "))
                if move < 0 or move > 8 or self.board[move] != -1:
                    raise ValueError
                return move
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

    def check_win(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 수평
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 수직
            [0, 4, 8], [2, 4, 6]              # 대각선
        ]
        for combination in win_combinations:
            if all(self.board[i] == player for i in combination):
                return True
        return False

    def print_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(map(str, self.board[i:i+3])))
            if i < 6:
                print("-" * 9)

    def quit_game(self):
        print("Game Over.")

# if __name__ == "__main__":
#     tictactoe = TicTacToe()
#     tictactoe.play_ttt()


# class TicTacToe:
#     def __init__(self):
#         self.board=[]#*9
#         for i in range(9):
#             self.board.append(-1)
        
#     def play_ttt(self):
#         pass
#     def getInput(self, turn):
#         pass
    def check_win(self):
        win_cord = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,9))
        for each in win_cord:
            if self.board[each[0]-1] == self.board[each[1]-1] and self.board[each[1]-1] == self.board[each[2] - 1]:
                return self.board[each[0] - 1]
        return -1


#         pass
#     def printBorad(self):
#         pass
#     def quit_game(self):
#         pass