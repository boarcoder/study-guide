"""
Given a log of website requests,
where each request entry contains (time, customerId, page visited).
Find the most visited n-consecutive page sequence. Where n can vary.

03:05:01-06/24/2024 | 1 | /homepage.htm
03:04:01-06/24/2024 | 1 | /shopping_cart.htm
03:02:01-06/24/2024 | 1 | /bananas.htm
03:01:01-06/24/2024 | 1 | /bananas.htm
03:01:01-06/24/2024 | 1 | /blueberries.htm
03:01:01-06/24/2024 | 1 | /apples.htm
"""

"""
1. We separate lists by customer_id.
2. A sequence n can be found with rolling hash on the page names
3. But what if n is longer/shorter? we have to make the rolling hash function support this theoretical
That means, L=List items, P=Unique pages, C=Unique customer, N=series pages tested

So the function should take in n as parameter.

"""
LOG_SPLIT_CH = "|"

"""
- TC: O(n log(n)) if the input log is not sorted by time. We must sort it.
- SC: O(n) if we place entire log into dic. But,
    O(c) if we just need to store 1 customer's visits at a time into dic.
    If this is too heavy, we can instead use O(n) space by splitting that into files,
    per customer, and only loading n lines from C files.

"""
from collections import deque


class PageSequenceData:
    def most_visited_n_conseq(self, page_sequence_log: str, n):
        dic_customer = {}
        dic_page = {}

        for line in page_sequence_log:
            time, customer_id, page_name = self._split_string(line)
            dic_page[page_name] = len(
                dic_page
            )  # assign a number to each page for easier hash.
            dic_customer[customer_id] = dic_customer.get(customer_id, []) + [
                time,
                dic_page[page_name],
            ]
        # now split by customer, we check all the rolling hashes counts.
        roll_deque = deque()
        dic_roll_hashes = {}
        for customer in dic_customer:
            customer_log = dic_customer[customer]
            dic_roll_hashes = {}
            roll_deque = deque(customer_log[0:n]) if n <= len(customer_log) else []
            if not roll_deque:
                continue

        pass

    def _get_rolling_hash(self, page_tup, i, n):
        # 1. If there is a timeout between page limit, we would invalidate a given roll,
        # and continue past that timeout page. But let's assume no timeout.

        # 2. Get initial rolling hash. We only need page id
        initial_view = (page_id for time, page_id in page_tup)

        for i in range(len(page_sequence) - n):
            pass
            # start_seq =

        pass

    def _hash_page(self, page_id: int):
        p = 31
        m = 10**9 + 7

    def _split_string(self, page_str: str):
        split = page_str.split(LOG_SPLIT_CH)
        if len(split) != 3:
            # Invalid, move on
            return None
        time, customer_id, page_name = split
        return (time, customer_id, page_name)
