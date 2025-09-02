'''
https://leetcode.com/problems/random-pick-with-weight/
I know python's random can actually select by weight. 
Let's assume the question is implement that method.

We would need to place weight as a number line element -

Number           0          2         3           n
Odds_cumulat     0.00      0.10       0.20        1.00

Then using random.uniform we can select a number between 0-1.
Binary search determines the selected number.
'''
import random
import bisect

class Solution:
    def __init__(self, w):
        self.cum_weight = []
        total = sum(w)
        cum = 0
        for weight in w:
            cum += weight/total
            self.cum_weight += [cum]

    def pickIndex(self) -> int:
        select = random.uniform(0.00, 1.00)
        print(f'select: {select}')
        print(f'self.cum_weight: {self.cum_weight}')
        return bisect.bisect_left(self.cum_weight, select)        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()