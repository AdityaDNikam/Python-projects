def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True, row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True, board[0][2]

    # Check for tie
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True, "tie"

    return False, None

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row number (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter column number (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("That position is already taken! Try again.")
            continue

        # Check for winner or tie
        game_over, winner = check_winner(board)
        if game_over:
            print_board(board)
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch player
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()