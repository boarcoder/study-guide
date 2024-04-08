'''

https://leetcode.com/problems/contains-duplicate/description/
'''


class Solution:
    def contains_duplicate(self, num_list):
        count_dic = {}

        for i, num_int in enumerate(num_list):
            count_dic[num_int] = count_dic.get(num_int, 0) + 1
            if count_dic.get(num_int) > 1:
                return True
        return False
            

# test/test_contains_duplicate.py
import unittest

class TestContainsDuplicate(unittest.TestCase):
    def setup(self):
        pass

    def test_1(self):
        num_list = [1,2,3,1]
        expected = True
        s = Solution()
        self.assertEqual(expected, s.contains_duplicate(num_list))

    def test_2(self):
        num_list = [1,2,3]
        expected = False
        s = Solution()
        self.assertEqual(expected, s.contains_duplicate(num_list))

    def test_3(self):
        num_list = []
        expected = False
        s = Solution()
        self.assertEqual(expected, s.contains_duplicate(num_list))

if __name__ == '__main__':
    unittest.main()