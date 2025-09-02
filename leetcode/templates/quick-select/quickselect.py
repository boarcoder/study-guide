"""
Quick Select
Uses: Kth largest

TC: O(n) average O(n^2) worst
SC:
"""

# elements to the left of L < pivot
# elements to the right of R > pivot
# k less than pivot: recurse left
# k larger than pivot: recurse right


def quickselect(arr, n, k):
    def partition(arr):
        L = 0
        R = n - 1
        while L < R:
            # smaller than pivot?
            if arr[L + 1] <= arr[L]:
                arr[L], arr[L + 1] = arr[L + 1], arr[L]
                L += 1
            elif arr[R] > arr[L]:
                R -= 1
            else:
                arr[R], arr[L + 1] = arr[L + 1], arr[R]
            return L

    p = partition(arr)
    if k == p:
        return arr[p]
    elif k < p:
        return quickselect(arr, p, k)
    else:
        return quickselect(arr, n - p + 1, k - p + 1)
