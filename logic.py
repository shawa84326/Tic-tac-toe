# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]  # Winner in a row
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]  # Winner in a column

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]  # Winner in the main diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]  # Winner in the other diagonal

    return None  # No winner yet



def other_player(player):
    return 'O' if player == 'X' else 'X'

    

    
