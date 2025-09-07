"""
Bingo card - 5x5

COLUMNS:
0. Values 1-15
1. 16-30
2. MIDDLE 31-45
3. 46-60
4. 61-75

col_start + random.uniform(0,14)
--
col_start + SortedSet(0,14)
O((n)log(n))

Matrix,
every value is randomly generated
unique values

------
Time complexity: O(5 * 5 log (5)) = O(1)
Space complexity: O(15 + log (5)) = O(1)
"""

from sortedcontainers import SortedSet
import random
import unittest


class Solution:
    def generate_bingocard_v2(self, col_count=5):
        grid = [[0 for j in range(col_count)] for i in range(col_count)]
        for j in range(col_count):
            col_set = self.generate_random_last_swap((j * 15 + 1), 5, 15)
            iterator_col = iter(col_set)
            for i in range(len(grid)):
                grid[i][j] = next(iterator_col)
        return grid

    def generate_bingocard(self, col_count=5):
        grid = [[0 for j in range(col_count)] for i in range(col_count)]
        for j in range(col_count):
            col_set = self.generate_random((j * 15 + 1), 5, 15)
            iterator_col = iter(col_set)
            for i in range(len(grid)):
                grid[i][j] = next(iterator_col)
        return grid

    def generate_random(self, start_num=1, count=5, max_options=15):
        res = set()
        sorted_set = SortedSet([i for i in range(0, max_options)])
        # num_set = set([i for i in range(0, max_options)])
        for i in range(count):
            choice_idx = random.randint(0, len(sorted_set))
            choice = sorted_set.__getitem__(choice_idx)
            res.add(choice + start_num)
            sorted_set.remove(sorted_set.__getitem__(choice_idx))
        return res

    def generate_random_last_swap(self, start_num=1, count=5, max_options=15):
        return random.sample([i for i in range(start_num, start_num + max_options)], count)

    def custom_random(self, a, b):
        return random.randint(a, b)


class TestBingoCard(unittest.TestCase):
    def test_1(self):
        random.seed(42)
        s = Solution()
        actual = s.generate_bingocard()
        self.assertEqual([[]], actual)
        print(f"{actual=}")


if __name__ == "__main__":
    print("file is running")
    unittest.main()
    print("unittest ran")
