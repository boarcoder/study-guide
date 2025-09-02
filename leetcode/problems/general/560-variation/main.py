'''
https://leetcode.com/problems/subarray-sum-equals-k/
[M] Pass 15m
Question:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Variation:
ONLY positive numbers.
SPACE optimal solution requested.

python -m unittest leetcode/560-variation/main.py
'''
from typing import List
import unittest

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        L, R = 0,0
        ct = 0

        cur_sum = 0
        while R < len(nums):
            cur_sum += nums[R]
            while cur_sum > k and L < R:
                cur_sum -= nums[L]
                L += 1
            if cur_sum == k:
                ct += 1
            R += 1
        return ct