"""
TC: O(N) for N tiles
SPC: O(1) for dic to store tile count.
https://leetcode.com/problems/valid-sudoku/
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for grid_row in range(3):
            for grid_col in range(3):
                if not self.is_valid_3_3_grid(board, grid_row * 3, grid_col * 3):
                    return False

        for i in range(len(board)):
            row_dic = {}
            for j in range(len(board[0])):
                tile = board[i][j]
                if not self.validate_unique_dic(tile, row_dic):
                    return False

        for j in range(len(board[0])):
            col_dic = {}
            for i in range(len(board)):
                tile = board[i][j]
                if not self.validate_unique_dic(tile, col_dic):
                    return False

        return True

    def is_valid_3_3_grid(self, board, i, j):
        grid_dic = {}
        for i1 in range(i, i + 3):
            for j1 in range(j, j + 3):
                tile = board[i1][j1]
                if not self.validate_unique_dic(tile, grid_dic):
                    return False
        return True

    def validate_unique_dic(self, tile, dic):
        if tile != "." and tile in dic:
            return False
        dic[tile] = True
        return True


# test/test_contains_duplicate.py
import unittest


class TestContainsSudoku(unittest.TestCase):
    def test_works_on_valid_sudoku(self):
        input_board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        s = Solution()
        expected = True
        actual = s.contains_sudoku(input_board)
        self.assertEqual(expected, actual)

    def test_works_on_falsy_board(self):
        input_board = [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]

        s = Solution()
        expected = False
        actual = s.contains_sudoku(input_board)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
    print("wow")
