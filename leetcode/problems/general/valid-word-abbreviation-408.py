'''
TC: O(n)
SC: O(1)
https://leetcode.ca/2017-01-11-408-Valid-Word-Abbreviation/
'''
NUMS_STR = "0123456789"


def is_valid_ch(word: str, ch: str, i: int):
    if i > len(word) or i < 0:
        return False
    if not word[i] == ch or ch == "*":
        return False
    return True


def word_abbreviation(word: str, abbr: str):
    # word index
    i = 0

    substr_len = 0
    substr_len_str = ""
    j = 0
    while j < len(abbr):
        if abbr[j] in NUMS_STR:
            # no leading zeroes
            if not substr_len_str and abbr[j] == "0":
                return False
            while abbr[j] in NUMS_STR and j < len(abbr):
                substr_len_str += abbr[j]
                j += 1
            else:
                substr_len = int(substr_len_str)
                substr_len_str = ""
                i += substr_len
            if not is_valid_ch(word, abbr[j], i):
                return False
        j += 1
        i += 1

    return True


import unittest


class TestWordAbbreviation(unittest.TestCase):
    def test_substition(self):
        """
        should give valid abbreviation for 'substitution'
        """
        word = "substitution"
        abbr = "s10n"
        expected = True
        actual = word_abbreviation(word, abbr)
        self.assertEqual(expected, actual)

    def test_internationalization(self):
        """
        should give valid abbreviation for 'substitinternationalizationution'
        """
        word = "internationalization"
        abbr = "i12iz4n"
        expected = True
        actual = word_abbreviation(word, abbr)
        self.assertEqual(expected, actual)

    def test_invalid_example(self):
        """
        should give invalid for 'apple'
        """
        word = "apple"
        abbr = "a2e"
        expected = False
        actual = word_abbreviation(word, abbr)
        self.assertEqual(expected, actual)


unittest.main()
