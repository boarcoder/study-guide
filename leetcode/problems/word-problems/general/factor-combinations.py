"""
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Guess:---------------------
Input: 9
Factors: [3]
Output: [9] as 3*3
---------------------------

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

"""

"""
TC: O(sqrt(n) * log(n))
SC: O(log(n)) - log(n) factor counts < sqrt(n)  as n / product > 2
[L]
254. Factor Combinations
https://algo.monster/liteproblems/254
"""


def is_valid_solution(factor_state_dic, target):
    return factor_state_dic["product"] == target


def get_candidates(factor_state_dic, target, current_f):
    res = []
    if factor_state_dic["product"] >= target:
        return []
    for f in factor_state_dic:
        if f == "product":
            continue
        if f < current_f:
            continue
        if target // f < 2:
            break
        res.append(f)
    return res


def solve(factor_state_dic, target, current_f, solution_list):
    if is_valid_solution(factor_state_dic, target):
        res = []
        for f in factor_state_dic:
            if f == "product":
                continue
            for _ in range(factor_state_dic[f]):
                res.append(f)
        solution_list.add(tuple(res))

    for c in get_candidates(factor_state_dic, target, current_f):
        factor_state_dic[c] += 1
        factor_state_dic["product"] *= c
        solve(factor_state_dic, target, current_f, solution_list)
        factor_state_dic[c] -= 1
        factor_state_dic["product"] /= c


def get_factors_list(n):
    factor_list = []
    for i in range(2, n // 2 + 1):
        # get all factors
        if n % i == 0:
            factor_list.append(i)
    return factor_list


def factor_combinations(n: int) -> list:
    factor_list = get_factors_list(n)
    if not factor_list:
        return []
    # associate possible states with counts of factors
    factor_state_dic = {f: 0 for f in factor_list}
    factor_state_dic["product"] = 1
    target = n
    solution_list = set()
    solve(factor_state_dic, target, factor_list[0], solution_list)
    res = []
    for el in solution_list:
        res.append(list(el))
    res.sort()
    return res


import unittest


class TestFactorCombinations(unittest.TestCase):
    def test_can_factor_1(self):
        n = 1
        expected = []
        actual = factor_combinations(n)
        self.assertEqual(expected, actual)

    def test_can_factor_37(self):
        n = 37
        expected = []
        actual = factor_combinations(n)
        self.assertEqual(expected, actual)

    def test_can_factor_9(self):
        n = 9
        expected = [[3, 3]]
        expected.sort()
        actual = factor_combinations(n)
        self.assertListEqual(expected, actual)

    def test_can_factor_12(self):
        n = 12
        expected = [[2, 6], [2, 2, 3], [3, 4]]
        expected.sort()
        actual = factor_combinations(n)
        self.assertListEqual(expected, actual)

    def test_can_factor_32(self):
        n = 32
        expected = [
            [2, 16],
            [2, 2, 8],
            [2, 2, 2, 4],
            [2, 2, 2, 2, 2],
            [2, 4, 4],
            [4, 8],
        ]
        expected.sort()
        actual = factor_combinations(n)
        self.assertEqual(expected, actual)


unittest.main()
