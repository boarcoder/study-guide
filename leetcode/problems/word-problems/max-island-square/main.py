'''
https://www.youtube.com/watch?v=Ti5vfu9arXQ

Option 1: BFS
If we exceed the bounds, we only do that if every tile before the bounds is good.

'''

from pprint import pprint
import unittest

GOOD = '1'
BAD = '0'

class Solution:
    def __init__(self):
        self.longest_diag = 0

    def max_island_square(self, board):
        # memo_element: down, right, diag
        memo_down = [[None for _ in board[0]] for _ in board]
        memo_right = [[None for _ in board[0]] for _ in board]
        memo_min_r = [[None for _ in board[0]] for _ in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                tile = board[i][j]
                if tile == GOOD:
                    self.dfs_down(board, i, j, memo_down)
                    self.dfs_right(board, i, j, memo_right)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if memo_down[i][j] is None:
                    memo_down[i][j] = 0
                if memo_right[i][j] is None:
                    memo_right[i][j] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                d = memo_down[i][j]
                min_r = float('inf')
                for k in range(d):
                    if memo_min_r[i+k][j] is None:
                        memo_min_r[i+k][j] = min(min_r, memo_right[i+k][j])
                    min_r = memo_min_r[i+k][j]
                self.longest_diag = max(self.longest_diag, min(d, min_r))
        return self.longest_diag ** 2
    
    def dfs_down(self, board, i, j, memo_down):
        # print('dfs downing', i, j)
        if i >= len(board) or j >= len(board[0]) or board[i][j] == 0:
            return -1
        if memo_down[i][j] is not None:
            return memo_down[i][j]
        memo_down[i][j] = self.dfs_down(board, i+1, j, memo_down) + 1
        return memo_down[i][j]
    def dfs_right(self, board, i, j, memo_right):
        if i >= len(board) or j >= len(board[0]) or board[i][j] == 0:
            return -1
        if memo_right[i][j] is not None:
            return memo_right[i][j]
        memo_right[i][j] = self.dfs_right(board, i, j + 1, memo_right) + 1
        return memo_right[i][j]

def convert_2darr(input_str: str):
    res = []
    input_str = input_str.strip(' \n')
    for row in input_str.split('\n'):
        row = row.strip(' ')
        res.append([])
        for ch in row.split(' '):
            res[-1].append(ch)
    return res
        
class TestClass(unittest.TestCase):
    def test_1(self):
        example = f'''
        0 1 1 0 1
        1 1 0 1 0
        0 1 1 1 0
        1 1 1 1 0
        1 1 1 1 1
        0 0 0 0 0
        '''
        s = Solution()
        expected = 9
        actual = s.max_island_square(convert_2darr(example))
        self.assertEqual(expected, actual)

    def test_2(self):
        example = f'''
        1 1 1 1 1
        1 1 1 1 0
        1 1 1 1 0
        1 1 1 1 0
        1 1 1 1 1
        0 0 0 0 0
        '''
        s = Solution()
        expected = 16
        actual = s.max_island_square(convert_2darr(example))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
