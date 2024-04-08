'''
Time: O(N)
Space: O(unique chs) = O(1) usually limited chs.

https://leetcode.com/problems/valid-anagram/description/
'''
def is_anagram(s, t):
    ch_dic = {}
    for i, ch in enumerate(s):
        ch_dic[ch] = ch_dic.get(ch, 0) + 1

    for i, ch in enumerate(t):
        ch_dic[ch] = ch_dic.get(ch, 0) - 1

    for key in ch_dic:
        if ch_dic[key] != 0:
            return False
    return True


import unittest

class TestIsAnagram(unittest.TestCase):
    def setup(self):
        pass

    def test_1(self):
        expected = True
        inputs = ['anagram', 'nagaram']
        self.assertEqual(expected, is_anagram(*inputs))

    def test_2(self):
        expected = False
        inputs = ['rat', 'car']
        self.assertEqual(expected, is_anagram(*inputs))

    def test_3(self):
        expected = True
        inputs = ['car', 'car']
        self.assertEqual(expected, is_anagram(*inputs))

if __name__ == '__main__':
    unittest.main()