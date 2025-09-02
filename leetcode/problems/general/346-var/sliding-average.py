'''
https://www.youtube.com/watch?v=aPD763eOAJ0
[M] 346. PASS 15min
TC:O(N) SC:O(1)

'''
from typing import List
def compute_running_sum_variant_346(nums: List[int], size: int) -> List[int]:
    window_sum = 0
    avg_windows = []
    for i in range(size):
        window_sum += nums[i]
    avg_windows += [window_sum // size]
    for i in range(len(nums) - size):
        window_sum -= nums[i]
        window_sum += nums[i + size]
        avg_windows += [window_sum // size]
    return avg_windows

if __name__ == '__main__':
    nums = [5, 2, 8, 14, 3]
    size = 3
    assert compute_running_sum_variant_346(nums, size) == [5, 8, 8]

    nums = [6]
    size = 1
    assert compute_running_sum_variant_346(nums, size) == [6]

    nums = [1, 2, 3]
    size = 1
    assert compute_running_sum_variant_346(nums, size) == [1, 2, 3]

    nums = [2, 4, 6, 8, 10, 12]
    size = 2
    assert compute_running_sum_variant_346(nums, size) == [3, 5, 7, 9, 11]

    nums = [2, 4, 6, 8, 10, 12]
    size = 6
    assert compute_running_sum_variant_346(nums, size) == [(2+4+6+8+10+12)/size]

    nums = [1, 2, 3, 4, 5]
    size = 4
    assert compute_running_sum_variant_346(nums, size) == [2, 3]

    nums = [1, 2, 1, 2]
    size = 2
    assert compute_running_sum_variant_346(nums, size) == [1, 1, 1]




