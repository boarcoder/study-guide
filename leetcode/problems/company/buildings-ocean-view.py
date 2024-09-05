import unittest

"""
TC: O(n)
SC: O(n with view)
ME
https://leetcode.ca/all/1762.html
"""


class Solution:
    def buildings_with_ocean_view(self, heights):
        local_max = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            if h > local_max:
                res.append(i)
                local_max = h
        return res[::-1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        """
        It should return correct num of buildings with ocean view with 0-index
        """
        heights = [4, 2, 3, 1]
        s = Solution()
        expected = [0, 2, 3]
        actual = s.buildings_with_ocean_view(heights)
        self.assertEqual(expected, actual)

    def test_2(self):
        """
        It should return if all buildings can see ocean
        """
        heights = [4, 3, 2, 1]
        s = Solution()
        expected = [0, 1, 2, 3]
        actual = s.buildings_with_ocean_view(heights)
        self.assertEqual(expected, actual)

    def test_3(self):
        """
        It should return only 1 building can see
        """
        heights = [1, 3, 2, 4]
        s = Solution()
        expected = [3]
        actual = s.buildings_with_ocean_view(heights)
        self.assertEqual(expected, actual)

    def test_4(self):
        """
        It should return 1 building can see because same height
        """
        heights = [4, 4, 4, 4]
        s = Solution()
        expected = [3]
        actual = s.buildings_with_ocean_view(heights)
        self.assertEqual(expected, actual)

    def test_5(self):
        """
        It should return only 2 building can see because a few same height
        """
        heights = [5, 4, 4, 4]
        s = Solution()
        expected = [0, 3]
        actual = s.buildings_with_ocean_view(heights)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
