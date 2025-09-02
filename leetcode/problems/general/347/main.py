from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # variation: return in frequency sorted order.
        # return self.heap_top_k(nums, k)
        return self.bucket_top_k(nums, k)

    def heap_top_k(self, nums, k):
        res = []
        count_dic = defaultdict(int)
        for num in nums:
            count_dic[num] += 1
        heap = [(-count_dic[num], num) for num in count_dic]
        heapq.heapify(heap)
        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        return res

    def bucket_top_k(self, nums, k):
        res = []
        count_dic = defaultdict(int)
        freq_dic = {i: [] for i in range(len(nums) + 1)}
        for num in nums:
            count_dic[num] += 1
        for num in count_dic:
            count = count_dic[num]
            freq_dic[count].append(num)
        for count in freq_dic:
            for num in freq_dic[count]:
                res.append(num)
        return res[-1 : -k - 1 : -1]
