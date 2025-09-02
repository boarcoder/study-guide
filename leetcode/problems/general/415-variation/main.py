'''
415 https://leetcode.com/problems/add-strings/
But it is floats.
'''

dic = {ch: i for i,ch in enumerate(list('0123456789'))}

import binarytree
from binarytree import Node

class Solution:
    def addStrings(self, num1: str, num2: str):
        # Split the numbers into integer and decimal parts
        if '.' in num1:
            int_part1, dec_part1 = num1.split('.')
        else:
            int_part1, dec_part1 = num1, '0'
            
        if '.' in num2:
            int_part2, dec_part2 = num2.split('.')
        else:
            int_part2, dec_part2 = num2, '0'
        
        # Add integer parts
        int_result = self.addIntegers(int_part1, int_part2)
        
        # Pad decimal parts to the same length
        max_len = max(len(dec_part1), len(dec_part2))
        dec_part1 = dec_part1.ljust(max_len, '0')
        dec_part2 = dec_part2.ljust(max_len, '0')
        
        # Add decimal parts
        dec_result = self.addIntegers(dec_part1, dec_part2)
        
        # If decimal result has more digits than max_len, carry to integer part
        if len(dec_result) > max_len:
            int_result = self.addIntegers(int_result, dec_result[0])
            dec_result = dec_result[1:]
        
        return f'{int_result}.{dec_result}'
    
    def addIntegers(self, num1: str, num2: str) -> str:
        """Add two non-negative integers represented as strings"""
        result = []
        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1
        
        while p1 >= 0 or p2 >= 0:
            x1 = dic[num1[p1]] if p1 >= 0 else 0
            x2 = dic[num2[p2]] if p2 >= 0 else 0
            
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            
            result.append(str(value))
            p1 -= 1
            p2 -= 1
        
        if carry:
            result.append(str(carry))
            
        return ''.join(result[::-1])


import unittest

class TestBinaryTree(unittest.TestCase):    
    def test_1(self):
        root = binarytree.build(
            [3,5,1,6,2,0,8,None,None,7,4]
            )
        s1 = "10.255555555555550"
        s2 = "1.33333"
        s = Solution()
        actual = s.addStrings(s1, s2)
        self.assertEqual('11.58889', actual)
        
if __name__ == '__main__':
    print('run tetts')
    unittest.main()
