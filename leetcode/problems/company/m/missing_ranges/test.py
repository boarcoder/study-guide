import unittest
from main import Solution


class TestInsertIntoCircularLinkedList(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        nums = [0, 1, 3, 50, 75]
        lower = 0
        upper = 99
        expected = ["2", "4->49", "51->74", "76->99"]
        actual = s.missing_ranges(nums, lower, upper)
        self.assertEqual(expected, actual)


unittest.main()
