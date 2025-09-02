'''
https://www.naukri.com/code360/problems/shortest-word-distance-ii_1459114
[A] 15m Time limit: Pass
TC: O(N)
SC: O(1)
'''
from os import *
from sys import *
from collections import *
from math import *

def minimumDistance(arr, book1, book2):
    L_book = None
    R_book = None
    L = 0
    R = 0
    # find 1st L_book. It is the first of either book.
    for L in range(len(arr)):
        if arr[L] == book1:
            L_book = book1
            R_book = book2
            R = L
            break
        if arr[L] == book2:
            L_book = book2
            R_book = book1
            R = L
            break
    if not L_book:
        return -1
    # Sliding window for smallest distance
    min_dist = float('inf')
    while R < len(arr):
        if arr[R] == R_book:
            if arr[L] == L_book:
                dist = R - L
                min_dist = min(min_dist, dist)
            if L < R:
                L += 1
            else:
                # swap the book referenced and start a new seek
                L_book, R_book = R_book, L_book
                L = R
                R = L + 1
        else:
            R += 1
    return min_dist
        

import unittest

class TestClas(unittest.TestCase):
    def test_1(self):
        pass
        
if __name__ == '__main__':
    print('run tetts')
    unittest.main()
