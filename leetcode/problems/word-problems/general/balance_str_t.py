"""
TC:
SC:

Balance str

str_input - 'xzyzxa'
output = 2

1. you can append characters
2. you can remove characte
"""

import heapq
import math

REMOVE_LAST_CH = "REMOVE_LAST_CH"
REMOVE_CH = "REMOVE_CH"
ADD_CH = "ADD_CH"


def get_max_freq(state):
    max_freq = -1
    for freq in state["freq_dic"]:
        max_freq = max(max_freq, freq)
    return max_freq


def remove_ch(state, ch):
    ct = state["ch_ct_dic"][ch]
    del state["freq_dic"][ct][ch]
    state["freq_dic"][ct - 1][ch] = True
    state["ch_ct_dic"][ch] -= 1
    return ch


def add_ch(state, ch):
    ct = state["ch_ct_dic"][ch]
    del state["freq_dic"][ct][ch]
    state["freq_dic"][ct + 1][ch] = True
    state["ch_ct_dic"][ch] += 1


def is_balanced_str(state):
    ct = None
    for ch in state["ch_ct_dic"]:
        if state["ch_ct_dic"][ch] == 0:
            continue
        if ct is None:
            ct = state["ch_ct_dic"][ch]
            continue
        if state["ch_ct_dic"][ch] != ct:
            return False
    return True


def is_valid_solution(state):
    return is_balanced_str(state)


def get_candidates(state, solution):
    res = []
    # print(f"state: {state}")
    if state["operations"] >= len(state["input_str"]):
        return res
    if state["operations"] >= solution["min_operations"]:
        return res
    if is_balanced_str(state):
        return res
    # 1. Delete a character in str
    max_freq = get_max_freq(state)
    for ch in state["ch_ct_dic"]:
        # print('state["ch_ct_dic"]', state["ch_ct_dic"], state["operations"])
        if state["ch_ct_dic"][ch] >= 1:
            res.append((REMOVE_CH, ch))
    # 2. Add a character to str, only if it is NOT in the max frequency
    for ch in state["ch_ct_dic"]:
        if ch not in state["freq_dic"][max_freq]:
            res.append((ADD_CH, ch))
    return res


def search(state, solution):
    if is_valid_solution(state):
        if state["operations"] > solution["min_operations"]:
            return
        solution["min_operations"] = min(
            solution["min_operations"], state["operations"]
        )

    for c in get_candidates(state, solution):
        operation, param = c
        if operation == REMOVE_CH:
            ch = param
            remove_ch(state, ch)
            state["operations"] += 1
            search(state, solution)
            state["operations"] -= 1
            add_ch(state, ch)
        elif operation == ADD_CH:
            ch = param
            add_ch(state, ch)
            state["operations"] += 1
            search(state, solution)
            state["operations"] -= 1
            remove_ch(state, ch)


# def balance_str(input_str: str):
#     freq_dic = {x: {} for x in range(100)}
#     ch_ct_dic = {}
#     ch_i_dic = {}

#     for i, ch in enumerate(input_str):
#         ch_i_dic[ch] = ch_i_dic.get(ch, []) + [i]
#         ch_ct_dic[ch] = ch_ct_dic.get(ch, 0) + 1

#     for ch in ch_ct_dic:
#         freq = ch_ct_dic[ch]
#         freq_dic[freq] = freq_dic.get(freq, {})
#         freq_dic[freq][ch] = True

#     state = {
#         "ch_ct_dic": ch_ct_dic,
#         "ch_i_dic": ch_i_dic,
#         "freq_dic": freq_dic,
#         "operations": 0,
#         "input_str": input_str,
#     }
#     solution = {"min_operations": float("inf")}

#     search(state, solution)
#     return solution["min_operations"]


# def balance_str(input_str: str):
#     # iterative solution, partitioning
#     ch_ct_dic = {}
#     for ch in input_str:
#         ch_ct_dic[ch] = ch_ct_dic.get(ch, 0) + 1

#     heap = []
#     for ch in ch_ct_dic:
#         heap.append((-ch_ct_dic[ch], ch))
#     heapq.heapify(heap)

#     operations = 0
#     first = heapq.heappop(heap)[0]
#     while heap:
#         cur_ct, cur_ch = heapq.heappop(heap)
#         operations += min((-cur_ct), -first - (-cur_ct))


def balance_str(input_str: str):
    ch_ct_dic = {}
    ct_sum = len(input_str)
    for ch in input_str:
        ch_ct_dic[ch] = ch_ct_dic.get(ch, 0) + 1

    average_ch_ct = ct_sum / len(ch_ct_dic)

    ops = 0.0
    for ch in ch_ct_dic:
        diff = (ch_ct_dic[ch] - average_ch_ct) / len(ch_ct_dic)
        ops += abs(diff)

    return math.ceil(ops)


"""
[b:2, a:4, z:11]

first = z:11
ops += min(4, 11-4)
ops += min(2, 11-2)

"""


# def recursive_bal_str(input_str: str, operation_ct):
#     if is_balanced_str(input_str):
#         return operation_ct

#     # try removal of a ch.
#     for i in range(len(input_str)):


#     # return min(operation_ct,)


# def balance_str_dp(input_str: str):
#     ch_ct_dic = {}
#     for i, ch in enumerate(input_str):
#         ch_ct_dic[ch] = ch_ct_dic.get(ch, 0) + 1

#     recursive_bal_str(input_str, )


import unittest


class TestBalanceStr(unittest.TestCase):
    def test_1(self):
        start_str = "ababc"
        expected = 1  # abab rem 1 c

        actual = balance_str(start_str)
        self.assertEqual(expected, actual)

    def test_2(self):
        start_str = "baaaaaba"
        expected = 2  # rem 2 b

        actual = balance_str(start_str)
        self.assertEqual(expected, actual)

    def test_3(self):
        start_str = "baaaaaba"
        expected = 2

        actual = balance_str(start_str)
        self.assertEqual(expected, actual)

    def test_4(self):
        start_str = "baaaaaba"
        expected = 2

        actual = balance_str(start_str)
        self.assertEqual(expected, actual)

    def test_5(self):
        start_str = "ba"
        expected = 0

        actual = balance_str(start_str)
        self.assertEqual(expected, actual)

    def test_6(self):
        start_str = "aaaabab"
        expected = 2

        actual = balance_str(start_str)
        self.assertEqual(expected, actual)


unittest.main()
