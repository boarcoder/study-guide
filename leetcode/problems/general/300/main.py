from sortedcontainers import SortedDict


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        longest_sub = 0
        dic = SortedDict()

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            idx = dic.bisect_right(num)
            larger_ct = 0
            print(f"{dic=}")
            if idx < len(dic):
                larger_num, larger_ct = dic.popitem(idx)
                dic[larger_num] = larger_ct
                larger_ct += 1
                print(f"{num=} {larger_num=} {larger_ct=}")
            longest_sub = max(longest_sub, larger_ct + 1)
            dic[num] = larger_ct
        return longest_sub


s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

# s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
