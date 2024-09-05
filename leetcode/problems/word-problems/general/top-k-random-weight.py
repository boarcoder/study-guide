"""
TC:
SC:

[A]
# Top k random weighted

- List of customers, with number of raffle tickets.
- Select k random customers to win, their odds of winning is weighted to their total tickets.
"""

import random
from sortedcontainers import SortedDict


def top_k_random_weighted(customer_list, k):
    res = []
    sorted_dic = SortedDict()
    customer_list.sort(key=lambda x: x["tickets"])
    total_tickets = 0
    for customer in customer_list:
        sorted_dic[total_tickets] = customer["customer"]
        total_tickets += customer["tickets"]
    sorted_dic[total_tickets] = None

    for _ in range(k):
        winner_ticket = random.randint(0, total_tickets)
        winner_i = sorted_dic.bisect_left(winner_ticket)
        winner_element = sorted_dic.popitem(winner_i)
        removed_tickets = winner_element[0]
        res.append(winner_element)
        total_tickets -= removed_tickets

    return res


def run_prob_test(f, customer_list, k, i):
    res = {}
    for _ in range(i):
        sample_list = f(customer_list, k)
        print(sample_list)
        for el in sample_list:
            res[el[1]] = res.get(el[1], 0) + 1
    return res


import unittest


class TestKRandomWeighted(unittest.TestCase):
    def test_k_randoms(self):
        input_customer_list = [
            {"customer": 1, "tickets": 25},
            {"customer": 2, "tickets": 10},
            {"customer": 3, "tickets": 30},
            {"customer": 4, "tickets": 35},
            {"customer": 5, "tickets": 10},
        ]
        k = 3
        res = run_prob_test(top_k_random_weighted, input_customer_list, k, 100)
        print("res:", res)


unittest.main()
