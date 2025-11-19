from typing import List
import sys


class State:
    def __init__(self, positions):
        # self.board = board
        self.positions = positions


class Solution:
    def __init__(self):
        self._display_initialized = False
        self._cursor_hidden = False

    def solveSudoku(self, board: List[List[str]]) -> List[List[str]]:
        try:
            self._prepare_display()
            state = State(self.get_fill_positions(board))
            self.solve(board, state, 0)
            return board
        finally:
            if self._cursor_hidden:
                sys.stdout.write("\x1b[?25h")
                sys.stdout.flush()
                self._cursor_hidden = False

    def get_candidates(self, board, state, position_i):
        candidates = []
        for num in range(1, 10):
            if self.is_valid_candidate(board, state, position_i, str(num)):
                candidates.append(f"{num}")
        return candidates

    def solve(self, board, state, position_i):
        if position_i == len(state.positions):
            return True
        self.print_matrix(board, state, position_i)
        for c in self.get_candidates(board, state, position_i):
            i, j = state.positions[position_i]
            board[i][j] = c
            if self.solve(board, state, position_i + 1):
                return True
            board[i][j] = "."

    def is_valid_candidate(self, board, state, position_i, c):
        i, j = state.positions[position_i]
        for row in range(len(board)):
            tile = board[row][j]
            if tile == c:
                return False
        for col in range(len(board[0])):
            tile = board[i][col]
            if tile == c:
                return False
        for bi in range((i // 3) * 3, (i // 3) * 3 + 3):
            for bj in range((j // 3) * 3, (j // 3) * 3 + 3):
                tile = board[bi][bj]
                if tile == c:
                    return False
        return True

    def get_fill_positions(self, board):
        positions = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                tile = board[i][j]
                if tile == ".":
                    positions.append((i, j))
        return positions

    def print_matrix(self, board, state, position_i):
        sys.stdout.write("\x1b[H")
        for i in range(len(board)):
            row_tokens = []
            for j in range(len(board[0])):
                tile = board[i][j]
                if (i, j) == state.positions[position_i]:
                    row_tokens.append(f"[{tile}]")
                elif (i, j) in state.positions:
                    row_tokens.append(f"({tile})")
                else:
                    row_tokens.append(f" {tile} ")
            sys.stdout.write(" ".join(row_tokens) + "\n")
        sys.stdout.flush()

    def _prepare_display(self):
        if not self._display_initialized:
            sys.stdout.write("\x1b[2J\x1b[H")
            sys.stdout.flush()
            self._display_initialized = True
        if not self._cursor_hidden:
            sys.stdout.write("\x1b[?25l")
            sys.stdout.flush()
            self._cursor_hidden = True


test_board = [
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
sol = Solution()
sol.solveSudoku(test_board)
