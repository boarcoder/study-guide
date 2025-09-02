from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.que = deque()
        self.cur_sum = 0


    def next(self, val: int) -> float:
        self.que.append(val)
        self.cur_sum += val
        while len(self.que) > self.size:
            rem = self.que.popleft()
            self.cur_sum -= rem
        return self.cur_sum/len(self.que)

import unittest

class TestMovingAverage(unittest.TestCase):
    def test_basic_functionality(self):
        ma = MovingAverage(3)
        self.assertAlmostEqual(ma.next(1), 1.0)  # (1) / 1
        self.assertAlmostEqual(ma.next(10), 5.5)  # (1 + 10) / 2
        self.assertAlmostEqual(ma.next(3), 4.66667, places=5)  # (1 + 10 + 3) / 3
        self.assertAlmostEqual(ma.next(5), 6.0)  # (10 + 3 + 5) / 3

    def test_window_size_one(self):
        ma = MovingAverage(1)
        self.assertAlmostEqual(ma.next(5), 5.0)  # (5) / 1
        self.assertAlmostEqual(ma.next(10), 10.0)  # (10) / 1
        self.assertAlmostEqual(ma.next(-3), -3.0)  # (-3) / 1

    def test_negative_numbers(self):
        ma = MovingAverage(3)
        self.assertAlmostEqual(ma.next(-1), -1.0)  # (-1) / 1
        self.assertAlmostEqual(ma.next(-5), -3.0)  # (-1 + -5) / 2
        self.assertAlmostEqual(ma.next(-3), -3.0)  # (-1 + -5 + -3) / 3
        self.assertAlmostEqual(ma.next(2), -2.0)  # (-5 + -3 + 2) / 3

    def test_large_window_size(self):
        ma = MovingAverage(5)
        self.assertAlmostEqual(ma.next(1), 1.0)  # (1) / 1
        self.assertAlmostEqual(ma.next(2), 1.5)  # (1 + 2) / 2
        self.assertAlmostEqual(ma.next(3), 2.0)  # (1 + 2 + 3) / 3
        self.assertAlmostEqual(ma.next(4), 2.5)  # (1 + 2 + 3 + 4) / 4
        self.assertAlmostEqual(ma.next(5), 3.0)  # (1 + 2 + 3 + 4 + 5) / 5
        self.assertAlmostEqual(ma.next(6), 4.0)  # (2 + 3 + 4 + 5 + 6) / 5

    def test_large_inputs(self):
        ma = MovingAverage(3)
        self.assertAlmostEqual(ma.next(100000), 100000.0)  # (100000) / 1
        self.assertAlmostEqual(ma.next(200000), 150000.0)  # (100000 + 200000) / 2
        self.assertAlmostEqual(ma.next(300000), 200000.0)  # (100000 + 200000 + 300000) / 3
        self.assertAlmostEqual(ma.next(400000), 300000.0)  # (200000 + 300000 + 400000) / 3

    def test_edge_case_empty_stream(self):
        ma = MovingAverage(3)
        # No calls to `next` should result in no output, but this is handled by the class design.

    def test_edge_case_large_window(self):
        ma = MovingAverage(1000)
        for i in range(1, 1001):
            ma.next(i)  # Fill the window
        self.assertAlmostEqual(ma.next(1001), 501.5)  # Average of 2 to 1001

if __name__ == "__main__":
    unittest.main()