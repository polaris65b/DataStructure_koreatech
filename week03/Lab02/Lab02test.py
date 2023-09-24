from Lab02 import Matrix, EightQueens, TicTacToe

# Example usage:
matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

result = matrix1 + matrix2
print("Matrix Addition:")
print(result)

result = matrix1 - matrix2
print("Matrix Subtraction:")
print(result)

result = matrix1 * matrix2
print("Matrix Multiplication:")
print(result)

transposed_matrix = matrix1.transpose()
print("Transpose of Matrix 1:")
print(transposed_matrix)

print("Initial Board:")
queens = EightQueens()
queens.print_board()

print("\nSolved Board:")
queens.solve()
queens.print_board()

game = TicTacToe()
while not game.winner and not game.is_full():
    game.print_board()
    print(f"Current player: {game.current_player}")
    try:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        game.make_move(row, col)
    except (ValueError, IndexError):
        print("Invalid input. Try again.")

game.print_board()
if game.winner:
    print(f"Player {game.winner} wins!")
else:
    print("It's a draw!")