"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

"""


def weight_depth_sum(input_list: list):
    return recursive_sum(input_list, 0)


def recursive_sum(input_list, depth):
    if not input_list:
        return 0

    depth_sum = 0
    for element in input_list:
        if isinstance(element, int):
            depth_sum += (depth + 1) * element
        elif isinstance(element, list):
            depth_sum += recursive_sum(element, depth + 1)
    return depth_sum


import unittest


class TestWeightSum(unittest.TestCase):
    def test_sum_weighted_1(self):
        """
        Can sum a weighted list where depth * values
        """
        input_list = [[1, 1], 2, [1, 1]]
        expected = 10
        actual = weight_depth_sum(input_list)
        self.assertEqual(expected, actual)

    def test_sum_weighted_2(self):
        """
        Can sum a weighted list with one value per depth
        """
        input_list = [1, [4, [6]]]
        expected = 27
        actual = weight_depth_sum(input_list)
        self.assertEqual(expected, actual)

    def test_sum_weighted_3(self):
        """
        Can sum a weighted list with only 1 value depth
        """
        input_list = [[[3]]]
        expected = 9
        actual = weight_depth_sum(input_list)
        self.assertEqual(expected, actual)


unittest.main()
