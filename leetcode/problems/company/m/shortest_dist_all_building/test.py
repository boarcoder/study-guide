import unittest
from shortest_dist_all_building import Solution


class TestShortestDistAllBuilding(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        input_list = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        """
    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0
    """
        expected = 7
        actual = s.shortest_distance(input_list)
        self.assertEqual(expected, actual)

    def test_example2(self):
        s = Solution()
        input_list = [
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0],
        ]
        """
    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0
    """
        expected = 88
        actual = s.shortest_distance(input_list)
        self.assertEqual(expected, actual)


unittest.main()
