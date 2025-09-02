r"""
Source: CSCQ discord: amojaboori
Given a list of numbers, and threshold
Find the longest consequtive subarray,
where the largest and smallest element,
The difference does not exceed the threshold.
TC: O(n * log(n))
SC: O(n)
"""

import sortedcontainers


class Solution:
    def max_length_diff_subarray(self, num_list, threshold):
        max_len_subarr = 1
        L = 0
        R = 0
        sorted_dic = sortedcontainers.SortedDict()
        while R < len(num_list):
            cur_num = num_list[R]
            sorted_dic[cur_num] = sorted_dic.get(cur_num, 0) + 1
            cur_diff = sorted_dic.peekitem(-1)[0] - sorted_dic.peekitem(0)[0]
            if cur_diff > threshold:
                rem_num = num_list[L]
                sorted_dic[rem_num] = sorted_dic.get(rem_num, 0) - 1
                sorted_dic[cur_num] = sorted_dic.get(cur_num, 0) - 1
                if sorted_dic.get(rem_num, 0) == 0:
                    del sorted_dic[rem_num]
                L += 1
                continue
            # is it bigger than max_len_subarr?
            max_len_subarr = max(max_len_subarr, R - L + 1)
            R += 1

        return max_len_subarr


import unittest


class TestThreshold(unittest.TestCase):
    def test_1(self):
        num_list = [2, 4, 5, 1, 2, 3]
        threshold = 4

        expected_subarr = [2, 4, 5, 1, 2, 3]
        expected = 6

        s = Solution()
        actual = s.max_length_diff_subarray(num_list, threshold)
        self.assertEqual(expected, actual)

    def test_2(self):
        num_list = [10, 5, 1, 3]
        threshold = 2

        expected_subarr = [1, 3]
        expected = 2

        s = Solution()
        actual = s.max_length_diff_subarray(num_list, threshold)
        self.assertEqual(expected, actual)

    def test_3(self):
        num_list = [10, 1]
        threshold = 2

        expected_subarr = [10]
        expected = 1

        s = Solution()
        actual = s.max_length_diff_subarray(num_list, threshold)
        self.assertEqual(expected, actual)

    def test_4(self):
        num_list = [1, 2, 3, 10, 3, 4]
        threshold = 8

        expected_subarr = [2, 3, 10, 3, 4]
        expected = 5

        s = Solution()
        actual = s.max_length_diff_subarray(num_list, threshold)
        self.assertEqual(expected, actual)

    def test_5(self):
        num_list = [10, 1, 2, 3, 10]
        threshold = 3

        expected_subarr = [1, 2, 3]
        expected = 3

        s = Solution()
        actual = s.max_length_diff_subarray(num_list, threshold)
        self.assertEqual(expected, actual)


unittest.main()
