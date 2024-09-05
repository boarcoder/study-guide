"""
TC: O(n * m) for product - where n and m removed 0 value elements
SC: O(n) where n removed 0 value elements

[M]
Sparse vector dot product
https://www.youtube.com/watch?v=sQNN4xKC1mA
"""


class SparseVector:
    def __init__(self, vector_list: list[int]):
        self.vector_data_list = self._get_vector_from_list(vector_list)
        self.length = len(self.vector_data_list)

    def __getitem__(self, i):
        return self.vector_data_list[i]

    def dot_product(self, v2):
        if not isinstance(v2, SparseVector):
            raise Exception("Not a SparseVector provided")
        res = 0
        v1 = self.vector_data_list
        top = 0
        bot = 0
        while top < self.length and bot < self.length:
            i, top_el = v1[top]
            j, bot_el = v2[bot]
            if i == j:
                res += top_el * bot_el
                top += 1
                bot += 1
            if i < j:
                top += 1
            if i > j:
                bot += 1
        return res

    def _get_vector_from_list(self, vector_list: list[int]) -> list[tuple[int, int]]:
        res = []
        for i, elem in enumerate(vector_list):
            if elem != 0:
                res.append((i, elem))
        return res


import unittest


class TestSparseVector(unittest.TestCase):
    def test_vectors_1(self):
        sv1 = SparseVector([1, 2, 3, 4, 5])
        sv2 = SparseVector([6, 7, 8, 9, 10])
        expected = (1 * 6) + (2 * 7) + (3 * 8) + (4 * 9) + (5 * 10)
        actual = sv1.dot_product(sv2)
        self.assertEqual(expected, actual)

    def test_vectors_2(self):
        sv1 = SparseVector([0, 1, 0, 0, 0])
        sv2 = SparseVector([0, 0, 0, 0, 2])
        expected = 0
        actual = sv1.dot_product(sv2)
        self.assertEqual(expected, actual)


unittest.main()
