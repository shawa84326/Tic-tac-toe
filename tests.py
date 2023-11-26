import unittest
from logic import make_empty_board, get_winner, other_player

class TicTacToeTests(unittest.TestCase):
    def test_make_empty_board(self):
        board = make_empty_board()
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertEqual(len(row), 3)
            self.assertTrue(all(cell is None for cell in row))

    def test_other_player(self):
        self.assertEqual(other_player('X'), 'O')
        self.assertEqual(other_player('O'), 'X')

    def test_get_winner_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertIsNone(get_winner(board))

    def test_get_winner_horizontal(self):
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', None],
            [None, None, None],
        ]
        self.assertEqual(get_winner(board), 'X')

    def test_get_winner_vertical(self):
        board = [
            ['O', 'X', None],
            ['O', 'X', None],
            ['O', None, None],
        ]
        self.assertEqual(get_winner(board), 'O')

    def test_get_winner_diagonal(self):
        board = [
            ['X', 'O', None],
            ['O', 'X', None],
            [None, None, 'X'],
        ]
        self.assertEqual(get_winner(board), 'X')

if __name__ == '__main__':
    unittest.main()
