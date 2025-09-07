"""
Two arrays of the same length arr1, arr2, select
 one number from each with minimum sum.
 With the constraint that the
 index selected from the second array >= the index selected from the first array


i    0  1  2  3  4  5
a1   0, 1, 2, 3, 4
a2   2, 3, 4, 5, 6

i    0  1  2  3  4  5
a1   0, 1, 2, 3, 4
a2   -1, 6, 5, 2

i    0  1  2  3  4  5
a1   00, 01, 02, 03, 04
a2   -1, 06, 05, 02
                      i local_min=
    [in, in, in, in, in] <--- reverse postfix min

edge 1: the second array must be larger or handle if not.
"""


def minimum_sum_combine_arr(arr1: list, arr2: list):
    res = [None, None]
    min_sum = float("inf")
    if not arr1 or not arr2:
        return [None, None]
    postfix = [float("inf") for num in arr1]
    min_num = float("inf")
    for i in range(len(arr2) - 1, -1, -1):
        min_num = min(min_num, arr2[i])
        postfix[i] = min_num
    for i, num in enumerate(arr1):
        if num + postfix[i] < min_sum:
            res = [num, postfix[i]]
        min_sum = min(min_sum, num + postfix[i])
    return res


def minimum_sum_combine_arr_eitherarr(arr1: list, arr2: list):
    arr1_first = minimum_sum_combine_arr(arr1, arr2)
    arr2_first = minimum_sum_combine_arr(arr2, arr1)
    if sum(arr1_first) >= sum(arr2_first):
        return arr1_first
    return arr2_first


import unittest


class TestMinSumArr(unittest.TestCase):
    def test_1(self):
        """
        i    0  1  2  3  4  5
        a1   0, 1, 2, 3, 4
        a2   8, 6, 5, 2, 3
        dp2  2  2  2  2  5
        """
        expected = [0, 2]
        actual = minimum_sum_combine_arr([0, 1, 2, 3, 4], [8, 6, 5, 2, 3])
        self.assertListEqual(expected, actual)

    def test_2(self):
        """
        i    0  1  2  3  4  5
        a1   0, 1, 2, 3, 4
        a2   3, 4, 5, 6, 7
        dp2  2  2  2  2  5
        """
        expected = [0, 3]
        actual = minimum_sum_combine_arr([0, 1, 2, 3, 4], [3, 4, 5, 6, 7])
        self.assertListEqual(expected, actual)

    def test_3(self):
        """
        i    0  1  2  3  4  5
        a1   0, 1, 2,  3,  4
        a2   3, 4, 5, -1,  7
        dp2  2  2  2  2  5
        """
        expected = [0, -1]
        actual = minimum_sum_combine_arr([0, 1, 2, 3, 4], [3, 4, 5, -1, 7])
        self.assertListEqual(expected, actual)

    def test_4(self):
        expected = [100, 1]
        actual = minimum_sum_combine_arr([100, 100, 1], [1, 100, 100])
        self.assertListEqual(expected, actual)

    def test_5(self):
        expected = [100, 1]
        actual = minimum_sum_combine_arr([100, 100, 1, 2, 3, 4, -1], [1, 100, 100])
        self.assertListEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
