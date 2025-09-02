'''
TC: O(n)
SC: O(1)
https://leetcode.ca/2017-01-11-408-Valid-Word-Abbreviation/
'''
NUMS_STR = "0123456789"

def word_abbreviation(word: str, abbr: str):
    w = 0
    i = 0
    while i < len(abbr):
        num = 0
        n = 0
        while abbr[i] in '0123456789':
            num *= 10
            num += int(abbr[i])
            i += 1
            n += 1
        w += num
        if word[w] != abbr[i]:
            return False
        i += 1
        w += 1
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
