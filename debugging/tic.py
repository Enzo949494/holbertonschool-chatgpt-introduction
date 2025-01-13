#!/usr/bin/python3
def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.

    Parameters:
        board (list of list of str): The 3x3 game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner in the current board state.

    Parameters:
        board (list of list of str): The 3x3 game board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.

    Players alternate turns to place 'X' or 'O' on a 3x3 board.
    The game ends when a player wins or the board is full.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter values between 0 and 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                moves += 1

                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break

                if moves == 9:
                    print_board(board)
                    print("It's a tie!")
                    break

                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except IndexError:
            print("Invalid input. Please enter values between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
