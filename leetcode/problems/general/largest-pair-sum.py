"""
Given `arr: list[int]` of numbers, return the largest possible sum
of every number within `k: int` unique pairs.
- A unique pair contains numbers from unique indices.
- The numbers in pairs do not have to be unique.
- The order matters - pairs containing the numbers from
    indices (1,2) and (2,1) are considered unique.
- Reusing an index, like (2,2), also produces a unique pair.

## Example Input:
arr = [9, 8, 1, 2, 3, 4, 2]
k = 3

## Example solution:
max_sum_pairs = [(9,9), (9,8), (8,9)]
expected = 52

"""

import unittest


"""
tc: O(n log k)
sc: O(k)
"""
import heapq


class UniqueIterable(list):
    """
    Ensures the first k elements in a given iterator are unique.
    """

    def __init__(self, arr: list, k: int):
        self.iterator = iter(arr)
        self.k = k
        self.set = set()

    def __iter__(self):
        return self

    def __next__(self):
        while self.k > 0 and ((next_unique := next(self.iterator)) in self.set):
            # print("addig", self.k, next_unique)
            continue
        if not next_unique:
            print("couldnt get next_unique")
        if self.k > 0:
            self.k -= 1
            self.set.add(next_unique)
        return next_unique


class Solution:
    def largest_pair_sum(arr: list[int], k: int) -> int:
        largest_sum = 0
        for el in UniqueIterable(arr, k):
            print("[", el)
        return None
        sorted_list = heapq.nlargest(k, UniqueIterable(arr, k))
        remain = k
        print("\n  sorted_list: ", sorted_list)
        n = 0
        a = 0
        res = []
        while a < len(sorted_list) and remain:
            b = a
            while b < len(sorted_list) and remain:
                c = b
                cur_pair = sorted_list[c] * 2
                if a + 1 < len(sorted_list) and sorted_list[b] + sorted_list[a + 1] > cur_pair:
                    a += 1
                    res += [[sorted_list[b], sorted_list[c]]]
                    largest_sum += sorted_list[b] + sorted_list[c]
                    n += 1
                    print("n:", n)
                    break
                while c < len(sorted_list) and remain:
                    cur_pair = sorted_list[b] + sorted_list[c]
                    if b + 1 < len(sorted_list) and sorted_list[b + 1] * 2 > cur_pair:
                        res += [[sorted_list[b + 1], sorted_list[b + 1]]]
                        largest_sum += sorted_list[b + 1] + sorted_list[b + 1]
                        remain -= 1
                        b += 1
                        n += 1
                        print("n:", n)
                    else:
                        res += [[sorted_list[b], sorted_list[c]]]
                        largest_sum += sorted_list[b] + sorted_list[c]
                        remain -= 1
                    if b != c and remain:
                        res += [[sorted_list[c], sorted_list[b]]]
                        largest_sum += sorted_list[c] + sorted_list[b]
                        remain -= 1
                    # print(a, b, c, largest_sum)
                    c += 1
                b += 1
            a += 1
        print("example list res:", res, "largest_sum:", largest_sum)
        return largest_sum


class TestLargestPairSum(unittest.TestCase):
    def test_1(self):
        arr = [9, 8, 1, 2, 3, 4, 2]
        k = 2
        expected = 35
        actual = Solution.largest_pair_sum(arr, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        arr = [9, 8, 1, 2, 3, 4, 2]
        k = 4
        expected = 68
        actual = Solution.largest_pair_sum(arr, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        arr = [-1, -5, 0, 2, 5]
        #   (5+5)=10, (5+2)=7, (2+5)=7 => total 24
        k = 3
        expected = 24
        actual = Solution.largest_pair_sum(arr, k)
        self.assertEqual(actual, expected, f"Expected sum of {expected}, got {actual}.")

    def test_4(self):
        arr = [-1, -5, 0, 2, 5, 7, 10, 100, 2, 1]
        #   (5+5)=10, (5+2)=7, (2+5)=7 => total 24
        k = 25
        expected = 1955
        actual = Solution.largest_pair_sum(arr, k)
        self.assertEqual(actual, expected, f"Expected sum of {expected}, got {actual}.")

    def test_5(self):
        arr = [
            999999999,
            -12345,
            0,
            99999999,
            42,
            42,
            42,
            999999998,
            -999999999,
            1000000,
            -1000000,
            987654321,
            123456789,
            444444444,
            222222222,
            111111111,
            333333333,
            -333333333,
            777777777,
            555555555,
            666666666,
            -666666666,
            314159265,
            161803398,
            141421356,
            271828182,
            -101010101,
            999999999,
            999999999,
            999999998,
            420,
            123,
            9999,
            10000,
            -42,
            12345,
            54321,
            98765,
            56789,
            888888888,
        ]
        # We'll just pick a moderate k:
        k = 10
        expected = 18839506153
        actual = Solution.largest_pair_sum(arr, k)
        self.assertEqual(actual, expected, f"Expected sum of {expected}, got {actual}.")


unittest.main()
