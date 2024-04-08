import unittest


# def words_num_sort(str_words: str):
#     list_words = str_words.split(" ")

#     def sort_num_in_str(x: str):
#         for i in range(len(x)):
#             ch = x[i]
#             if ch in "123456789":
#                 return int(ch)
#         return -1


#     list_words.sort(key=sort_num_in_str)
#     return " ".join(list_words)
def words_num_sort(str_words: str):
    dic = {i: None for i in range(1, 10)}
    for word in str_words.split(" "):
        for ch in word:
            if ch in "123456789":
                dic[int(ch)] = word
                continue
    return " ".join([dic[k] for k in dic if dic[k] is not None])


class TestWordsNumSort(unittest.TestCase):
    def test_sorts_str_1(self):
        expected = "Fo1r the2 g3ood 4of th5e pe6ople"
        actual = words_num_sort("4of Fo1r pe6ople g3ood th5e the2")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
