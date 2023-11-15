from logic import make_empty_board, get_winner, other_player

def print_board(board):
    for row in board:
        print(" | ".join([cell if cell else " " for cell in row]))
        print("-" * 9)

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
            print_board(board)
            print(f"Player {winner} wins!")
        elif all(all(cell for cell in row) for row in board):
            print_board(board)
            print("It's a draw!")
            break
        else:
            player = other_player(player)

if __name__ == '__main__':
    main()
