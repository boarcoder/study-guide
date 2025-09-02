'''
[M] Not ON LC

Question: Add two strings. They may each contain a decimal number

Trick: I think the point of this question might to demonstrate why banks would use a different
variable for decimal places.
'''
class Solution:
    # def add_string_decimal(self, str1: str, str2: str):
    #     num1, dec1 = self.string_to_float_sep(str1)
    #     num2, dec2 = self.string_to_float_sep(str2)

    #     return 



    def string_to_float_sep(self, float_str: str):
        before_total = 0
        after_total = 0
        before_dot = 0
        after_dot = 0
        cur = "before"

        # for ch in reversed(str1):
        
            if ch == '.' and cur == "after":
                cur = "before"
                continue
            # anything after the decimal place: .001
            if cur == "after":
                after_total += int(ch) * 10 ** after_dot
                after_dot += 1
                
            # anything before the decimal place: 100.
            if cur == "before":
                before_total += int(ch) * 10 ** before_dot
                before_dot += 1

        return before_total, after_total

            

                



import unittest

class TestClass(unittest.TestCase):
    def test_1(self):
        str1 = "400.1235"
        str2 = "23.45312312345"
        expected = float(str1) + float(str2)
        s = Solution()
        actual = s.add_string_decimal(str1, str2)
        self.assertEqual(expected, actual)

        
if __name__ == '__main__':
    print('run tetts')
    unittest.main()
