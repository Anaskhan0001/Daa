# Function to check if placing queen is safe
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve the problem
def solve_queens(board, col):
    if col >= len(board):
        return True  # All queens placed

    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen

            if solve_queens(board, col + 1):
                return True  # Success, move to next column

            board[row][col] = 0  # Backtrack

    return False  # No solution from this state

# Function to display the board
def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

# ---------------------------------------------
# Main Program

# Create empty 8x8 board
board = [[0 for _ in range(8)] for _ in range(8)]

# Place first Queen manually (Example: Row 0, Column 0)
first_row = int(input("Enter row (0-7) for first Queen: "))
first_col = int(input("Enter column (0-7) for first Queen: "))
board[first_row][first_col] = 1

# Solve from next column
if solve_queens(board, first_col + 1):
    print("\nFinal 8-Queens Board:")
    print_board(board)
else:
    print("Solution not possible from this starting point.")
