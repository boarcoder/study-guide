"""
TC:
SC:

Transpose Anagram

Write a function that takes start_str, end_str, and returns a list of strings,
where each string in this list is the result of transposing two adjacent characters.
The return list is the operations taken to swap enough characters in start_str so that it equals end_str.
Or return if this is not possible.

APPLE -> PLEAP
"""

import time


def move_ch(i: int, target_i: int, cur_list: list):
    j = i
    # move ch forward
    if j < target_i:
        tmp = cur_list[j + 1]
        cur_list[j + 1] = cur_list[j]
        cur_list[j] = tmp
        j += 1
    if j > target_i:
        tmp = cur_list[j - 1]
        cur_list[j - 1] = cur_list[j]
        cur_list[j] = tmp
        j -= 1
    return j, cur_list


def transpose_anagram(start_str: str, end_str: str):
    # get index for each ch
    res = [start_str]
    dic_ch = {}
    start_ch = {}
    for i, ch in enumerate(end_str):
        dic_ch[ch] = dic_ch.get(ch, []) + [i]

    for i, ch in enumerate(start_str):
        start_ch[ch] = start_ch.get(ch, 0) + 1

    for key in dic_ch:
        if len(dic_ch[key]) != start_ch[key]:
            raise Exception("Not possible as strings are not anagrams!")

    cur_list = list(start_str)
    print(f"cur_list: {cur_list}")
    len_cur = len(cur_list)

    for i in range(len_cur):
        ch = cur_list[i]
        if "".join(cur_list) != end_str:
            if dic_ch[ch]:
                target_i = dic_ch[ch].pop()
                print(f"target_i: {target_i}")
                j = i
                while j != target_i:
                    j, cur_list = move_ch(j, target_i, cur_list)
                    res.append("".join(cur_list))
                    time.sleep(0.3)
                    print(f"j: {j} target: {target_i}, cur_list: {cur_list}")
            res.append("".join(cur_list))
    return res


import unittest


class TestTransposeAnagram(unittest.TestCase):
    def test_apple(self):
        start_str = "apple"
        end_str = "pleap"
        expected = [
            "apple",
            "paple",
            "ppale",
            "pplae",
            "pplae",
            "plpae",
            "plape",
            "plaep",
            "plaep",
            "plaep",
            "pleap",
            "pleap",
        ]
        actual = transpose_anagram(start_str, end_str)
        self.assertEqual(expected, actual)

    def test_bug(self):
        start_str = "bug"
        end_str = "gub"
        expected = ["bug", "ubg", "ugb", "ugb", "gub", "gub"]
        actual = transpose_anagram(start_str, end_str)
        self.assertEqual(expected, actual)

    def test_racecar(self):
        # should return error if not possible
        start_str = "racecar"
        end_str = "raraceac"
        expected = "raraceac"
        actual = transpose_anagram(start_str, end_str)
        self.assertEqual(expected, actual)


unittest.main()
