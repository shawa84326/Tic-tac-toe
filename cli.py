from logic import make_empty_board, get_winner, other_player
import csv
import os

LOGS_DIR = "logs"
LOG_FILE = os.path.join(LOGS_DIR, "database.csv")

def print_board(board):
    for row in board:
        print(" | ".join([cell if cell else " " for cell in row]))
        print("-" * 9)
def record_winner(player):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player])
def get_user_move():
    while True:
        try:
            move = input("Enter your move (row,col): ")
            row, col = map(int, move.split(','))
            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Please enter in the format 'row,col'.")

def main():
    
    board = make_empty_board()
    player = 'X'
    winner = None

    while not winner:
        print_board(board)
        print(f"Player {player}'s turn.")

        row, col = get_user_move()

        if board[row][col] is not None:
            print("Cell already taken. Try again.")
            continue

        board[row][col] = player
        winner = get_winner(board)
        
        if winner:
            record_winner(winner)
            print_board(board)
            print(f"Player {winner} wins!")
        elif all(all(cell for cell in row) for row in board):
            record_winner("Draw")
            print_board(board)
            print("It's a draw!")
            break
        else:
            player = other_player(player)

if __name__ == '__main__':
    main()
