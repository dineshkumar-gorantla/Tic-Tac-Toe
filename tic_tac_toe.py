import numpy as np

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

# Function to check if the board is full (draw)
def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1  # X wins
    elif winner == PLAYER_O:
        return -1  # O wins
    elif is_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for X
def find_best_move(board):
    best_move = (-1, -1)
    best_score = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Main game loop
def main():
    board = np.full((3, 3), EMPTY)
    current_player = PLAYER_O  # Let O go first

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            row, col = find_best_move(board)
            board[row][col] = PLAYER_X
            print(f"Player X plays at ({row}, {col})")
        else:
            # Player O's turn (user input)
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if board[row][col] == EMPTY:
                        board[row][col] = PLAYER_O
                        break
                    else:
                        print("Cell already taken! Choose another.")
                except (IndexError, ValueError):
                    print("Invalid input! Please enter 0, 1, or 2.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    main()
