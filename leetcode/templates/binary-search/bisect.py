"""
TC: O(log(N))
SPC: O(1)
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
-----
"""


def bisect_left(arr, target, lo=0, hi=None, key=lambda val: val):
    if hi is None:
        hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2

        if key(arr[mid]) < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(arr, target, lo=0, hi=None, key=lambda val: val):
    if hi is None:
        hi = len(arr)

    while lo < hi:
        mid = (lo + hi) // 2

        if key(arr[mid]) <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


"""
bisect_left returns the leftmost inclusive position where target MAY be. 
bisect_right returns the rightmost position, +1 to the right of the target, if it MAY be in the arr.
Verify target (return is in bounds too) after using.

key parameter. default is just the value. But you can apply a function such that key function
returns a different value, that is compared to target.


"""


def example_bin_search():
    arr = [0, 1, 2, 3]
    target = 2
    left_i = bisect_left(arr, target)
    if left_i < len(arr) and arr[left_i] == target:
        return left_i


"""
For fun: how to use a condition with bisect.
Just make the key function return the conditional evaluation.
Set target to True (condition == True)
"""


def condition(elem):
    return elem == "cool"


bisect_left(arr, True, key=condition)
