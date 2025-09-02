import unittest
from solution import Solution  # Make sure your solution code is in solution.py


class TestProductOfTwoRLEArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        encoded1 = [[1, 3], [2, 3]]
        encoded2 = [[6, 3], [3, 3]]
        expected_output = [[6, 6]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_example2(self):
        encoded1 = [[1, 3], [2, 1], [3, 2]]
        encoded2 = [[2, 3], [3, 3]]
        expected_output = [[2, 3], [6, 1], [9, 2]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_empty_arrays(self):
        encoded1 = []
        encoded2 = []
        expected_output = []
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_single_element_arrays(self):
        encoded1 = [[5, 1]]
        encoded2 = [[4, 1]]
        expected_output = [[20, 1]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_different_frequencies(self):
        encoded1 = [[2, 5]]
        encoded2 = [[3, 2], [4, 3]]
        expected_output = [[6, 2], [8, 3]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_large_numbers(self):
        encoded1 = [[100000, 100000]]
        encoded2 = [[100000, 100000]]
        expected_output = [[10000000000, 100000]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_alternating_values(self):
        encoded1 = [[1, 2], [2, 2], [1, 2], [2, 2]]
        encoded2 = [[2, 4], [3, 4]]
        expected_output = [[2, 2], [4, 2], [3, 2], [6, 2]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)

    def test_non_overlapping_frequencies(self):
        encoded1 = [[1, 2], [2, 3]]
        encoded2 = [[3, 5]]
        expected_output = [[3, 2], [6, 3]]
        output = self.solution.findRLEArray(encoded1, encoded2)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
