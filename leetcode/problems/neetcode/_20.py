import unittest

"""
Example 1: 

input = 'asdf'

expected = 'fdsa'

actual = reverse_string(input)

"""


class TestClass(unittest.TestCase):
    def test_should_check_parentheses_valid_1(self):
        """
        Should return True on valid paren
        """
        solution = Solution()
        expected = True
        actual = solution.isValid("(())")
        self.assertEqual(expected, actual)

    def test_should_check_parentheses_valid_2(self):
        """
        Should return True on valid paren
        """
        solution = Solution()
        expected = True
        actual = solution.isValid("(([]))")
        self.assertEqual(expected, actual)

    def test_should_check_parentheses_valid_3(self):
        """
        Should return False on invalid paren
        """
        solution = Solution()
        expected = False
        actual = solution.isValid("(([]{))}")
        self.assertEqual(expected, actual)


class Solution:
    def isValid(self, s: str) -> bool:
        need_stack = []
        closing_dic = {
            "[": "]",
            "{": "}",
            "(": ")",
        }

        for ch in s:
            if closing_dic.get(ch, False):
                need_stack.append(closing_dic[ch])
            elif need_stack and need_stack[-1] == ch:
                need_stack.pop()
            else:
                return False

        if need_stack:
            return False
        return True


unittest.main()
