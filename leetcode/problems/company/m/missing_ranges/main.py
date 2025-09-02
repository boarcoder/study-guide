"""
https://leetcode.ca/all/708.html
Ref: M
TC: O(N) insert worst case
SC: O(1) insert
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next if next else self


class Solution:
    def missing_ranges(self, nums_list: list[int], lower: int, upper: int):
        res = []
        if not nums_list:
            return res
        nums_list.sort()
        prev = lower
        for num in nums_list + [upper + 1]:
            # the range was broken.
            if num > prev + 1:
                res += [self._range_to_str((prev + 1, num - 1))]
            # the range continues
            prev = num

        return res

    def _range_to_str(self, range_tup: tuple[int, int]):
        lo, hi = range_tup
        if lo == hi:
            return f"{lo}"
        return f"{lo}->{hi}"
