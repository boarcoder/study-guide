"""
The given problem presents us with a string s that consists of parentheses
('(' and ')') and lowercase English letters.
Our goal is to make the string a valid parentheses string by removing the fewest number
of parentheses possible. The criteria for a valid parentheses string is:

It is an empty string, or
It contains only lowercase characters, or
It can be written in the form of AB, where A and B are valid strings, or
It can be written in the form of (A), where A is a valid string.
Ultimately, we must ensure that every opening parenthesis '(' has a corresponding closing parenthesis ')', and there are no extra closing parentheses without a matching opening one.

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Requirement: O(1) space solution.
[m] FAIL: 30:00


[[0,0,0],
 [1,1,0],
 [1,1,1]]

 [[1,0,0],
  [1,1,0],
  [1,1,0]]



"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        paren_list = [ch for ch in s]
        return "".join(self.min_parentheses(paren_list))

    def min_parentheses(self, paren_list: list[str]):
        self.fix_paren_list(paren_list)
        self.fix_paren_list(paren_list, reverse=True)
        return paren_list

    def fix_paren_list(self, paren_list, reverse=False):
        L_CT = 0
        R_CT = 0
        iteration_range = range(len(paren_list))
        L_PAREN = "("
        R_PAREN = ")"
        if reverse:
            iteration_range = range(len(paren_list) - 1, -1, -1)
            L_PAREN = ")"
            R_PAREN = "("
        for i in iteration_range:
            ch = paren_list[i]
            if ch == L_PAREN:
                L_CT += 1
            if ch == R_PAREN:
                R_CT += 1
            if R_CT > L_CT:
                paren_list[i] = ""
                R_CT -= 1
