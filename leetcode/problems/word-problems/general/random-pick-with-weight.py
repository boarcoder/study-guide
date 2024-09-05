"""
TC:
SC:
[L]
https://leetcode.com/problems/random-pick-with-weight/description/
---
TC:
SC:

[A]
# Top k random weighted

- List of customers, with number of raffle tickets.
- Select k random customers to win, their odds of winning is weighted to their total tickets.
"""

"""
TC: O(N)
SC: O(N)
[L]
https://leetcode.com/problems/random-pick-with-weight/description/
"""
import random


class Solution:
    def __init__(self, w):
        self.list_weights = w
        self.total_probability = sum(w)
        self.index_list = [i for i in range(len(self.list_weights))]

    def pickIndex(self) -> int:
        choice_list = random.choices(self.index_list, self.list_weights, k=1)
        return choice_list[0]


"""
TC: O(N)
SC: O(N)
[L]
https://leetcode.com/problems/random-pick-with-weight/description/
"""
import random

import bisect


class Solution:
    def __init__(self, weight_list):
        # self.total_probability = sum(weight_list)
        self.cumulative_weights = []
        for i, w in enumerate(weight_list):
            self.cumulative_weights.append(
                (w + (weight_list[i - 1] if i - 1 > -1 else 0))
            )
        self.cumulative_weights.append(float("inf"))
        self.total_prob = sum(weight_list)

    """
    w         : [0.1, 0.1, 0.1]
    random.uniform(0, MAX)
    cumulative: [0.1, 0.2, 0.3] INFINITY
                  |
                  
    random.uniform(0,self.total_probability)
    """

    def pickIndex(self) -> int:
        random_weight = random.uniform(0, self.cumulative_weights[-2])
        i = bisect.bisect_left(self.cumulative_weights, random_weight)
        return i


#####################
import bisect


"""
TC: O(N) init, O(log(n)) for pickIndex,
SC: O(N) init, O(1) for pickIndex

The python function random.choices can do:
O(N) TC if weights
"""
import random


class Solution:
    def __init__(self, weight_list):
        self.total_prob = sum(weight_list)
        self.weight_list = weight_list
        self.cumulative_weights = []
        for i, w in enumerate(weight_list):
            self.cumulative_weights.append(
                (w + (self.cumulative_weights[i - 1] if i - 1 > -1 else 0))
            )
        # self.cumulative_weights.append(float("inf"))
        self.index_list = [i for i in range(len(self.weight_list))]

    def pickIndex(self) -> int:
        choices_list = random.choices(
            self.index_list,
            cum_weights=self.cumulative_weights,
            k=1,
        )
        return choices_list[0]


"""
TC:
SC:

[A]
# Top k random weighted

- List of customers, with number of raffle tickets.
- Select k random customers to win, their odds of winning is weighted to their total tickets.
- Once a customer wins, THEY ARE REMOVED from future raffles. (So if k=3, 3 unique customers).
"""
import random
import sortedcontainers


class Solution:
    def __init__(self, weight_list):
        self.total_prob = sum(weight_list)
        # self.weight_list = weight_list
        self.sorted_weight_list = sortedcontainers.sortedlist(weight_list)

        self.cumulative_weights = []
        for i, w in enumerate(self.sorted_weight_list):
            self.cumulative_weights.append(
                (w + (self.cumulative_weights[i - 1] if i - 1 > -1 else 0))
            )
        # self.cumulative_weights.append(float("inf"))
        self.index_list = [i for i in range(len(self.weight_list))]

    def pickIndex(self) -> int:
        choices_list = random.choices(
            self.index_list,
            cum_weights=self.cumulative_weights,
            k=1,
        )
        return choices_list[0]


weight_list = [0.1, 0.1, 0.3, 0.3, 0.2]
sorted_weight_list = [0.1, 0.1, 0.2, 0.3, 0.3]
cumulative_sorted_weight_list = [0.1, 0.2, 0.4, 0.7, 1.0]
r = [1.1, 1.2, 1.4, 1.7, 2.0]
#                                           | remove in o(log(n)) from both weight_list and cum_weight_list


total_prob = sum(weight_list)
weight_sorted_list = sortedcontainers.sortedlist(weight_list)
