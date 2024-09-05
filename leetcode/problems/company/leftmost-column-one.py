"""
TC: O(N * log(m)) N rows, M cols. We binary search for the column with the lowest 1 position.
SC: O(1)
1428. Leftmost Column with at Least a One
https://leetcode.ca/all/1428.html
[FAIL] > 15mins

1. Select a row. Bin search to find the leftmost 1.
2. For every REMAINING VALID row, check if it is a 1, if not, remove the row.
3. Select a REMAINING VALID row, repeat.
"""


class BinaryMatrixStub:
    def __init__(self, binary_matrix):
        self.binary_matrix = binary_matrix

    def get(self, row, col):
        return self.binary_matrix[row][col]

    def dimensions(
        self,
    ):
        n, m = len(self.binary_matrix), len(self.binary_matrix[0])
        return [n, m]


def bisect_left_custom(BinaryMatrix, x, lo, hi, row):
    while lo < hi:
        mid = (lo + hi) // 2
        if BinaryMatrix.get(row, mid) >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def leftmost_column_at_least_one(binary_matrix):
    # comment this for leetcode submission
    BinaryMatrix = BinaryMatrixStub(binary_matrix)
    # get matrix
    n, m = BinaryMatrix.dimensions()
    min_col = m
    MAX_COUNT = n * m
    counter = 0

    while counter < MAX_COUNT:
        counter += 1
        for row in range(n):
            if min_col < m and BinaryMatrix.get(row, min_col) != 1:
                continue
            leftmost_one = bisect_left_custom(BinaryMatrix, 1, 0, min_col, row)
            if leftmost_one < m and BinaryMatrix.get(row, leftmost_one) == 1:
                min_col = min(min_col, leftmost_one)
        if counter > MAX_COUNT:
            return "Too many calls. Use binary search."
        if min_col >= m:
            return -1
    return min_col


import unittest


class TestColumnAtLeastOne(unittest.TestCase):
    def test_should_give_col_0(self):
        "should give the column 0"
        input_matrix = [[0, 0], [1, 1]]
        expected = 0
        actual = leftmost_column_at_least_one(input_matrix)
        self.assertEqual(expected, actual)

    def test_should_give_col_1(self):
        "should give the column 1"
        input_matrix = [[0, 0], [0, 1]]
        expected = 1
        actual = leftmost_column_at_least_one(input_matrix)
        self.assertEqual(expected, actual)

    def test_should_give_no_col(self):
        "should give the column -1"
        input_matrix = [[0, 0], [0, 0]]
        expected = -1
        actual = leftmost_column_at_least_one(input_matrix)
        self.assertEqual(expected, actual)

    def test_should_give_col_1_bigger_matrix(self):
        "should give the column 1 bigger matrix"
        input_matrix = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
        expected = 1
        actual = leftmost_column_at_least_one(input_matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
