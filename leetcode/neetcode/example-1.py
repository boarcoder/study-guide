"""
Reverse a string function please

"""

"""
      i
i   0 1 2 3
str a s d f

res = 'fd'



"""


def reverse_string(string: str):
    res = ""
    for i in range(len(string) - 1, -1, -1):
        res += string[i]

    return res


# input = "asdf"
# expected = "fdsa"
# actual = reverse_string(input)
# print(f"""
#       input: {input}
#       expected: {expected}
#       actual: {actual}
#       """)

import unittest


class TestReverseString(unittest.TestCase):
    def test_reverses_a_string_1(self):
        input = "asdfg"
        expected = "gfdsa"
        actual = reverse_string(input)
        self.assertEqual(expected, actual)

    def test_reverses_a_string_2(self):
        input = ""
        expected = ""
        actual = reverse_string(input)
        self.assertEqual(expected, actual)

    def test_reverses_a_string_3(self):
        input = "123"
        expected = "321"
        actual = reverse_string(input)
        self.assertEqual(expected, actual)


unittest.main()
