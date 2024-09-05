"""
https://leetcode.ca/all/244.html
Shortest Word Distance II
                   L               R
[('makes', 1), ('coding', 3), ('makes', 4)]
[L]
TC: O(N)
SC: O(1)
"""


def shortest_word_distance(input_list, word_1, word_2):
    min_distance = float("inf")
    word_dic = {}

    combined_list = []
    for i, word in enumerate(input_list):
        if word == word_1 or word == word_2:
            tup = (word, i)
            combined_list.append(tup)

    print(f"combined_list: {combined_list}")
    L = 0
    R = 1
    while L < R and R < len(combined_list):
        a = combined_list[L]
        b = combined_list[R]
        if a[0] != b[0]:
            min_distance = min(min_distance, b[1] - a[1])
            L += 1
            R = L
        if b[1] - a[1] > min_distance:
            L = R
            R = L
        R += 1

    return min_distance


import unittest


class TestShortestWordDistance(unittest.TestCase):
    def test_word_distance_1(self):
        input_list = ["practice", "makes", "perfect", "coding", "makes"]
        word_1 = "coding"
        word_2 = "practice"

        expected = 3
        actual = shortest_word_distance(input_list, word_1, word_2)
        self.assertEqual(expected, actual)

    def test_word_distance_2(self):
        input_list = ["practice", "makes", "perfect", "coding", "makes"]
        word_1 = "makes"
        word_2 = "coding"

        expected = 1
        actual = shortest_word_distance(input_list, word_1, word_2)
        self.assertEqual(expected, actual)


unittest.main()
