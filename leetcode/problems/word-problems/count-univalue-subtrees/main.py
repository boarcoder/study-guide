'''
LC prem 250
https://www.naukri.com/code360/problems/unival-trees_697311
[M] 15m Time limit: Pass
TC: O(N)
SC: O(h)
'''

import binarytree
import queue
import sys
sys.setrecursionlimit(10**6)

def countUnivalTrees(root):
    ref = {'count': 0}
    dfs(root, ref)
    return ref['count']

def dfs(node, ref):
    if not node:
        return None
    L = dfs(node.left, ref)
    R = dfs(node.right, ref)
    if L in [node.val, None] and R in [node.val, None]:
        ref['count'] += 1
        return node.val
    return binarytree.Node(-1)
    # if not local
    # return BinaryTreeNode(-1)

import unittest

class TestBinaryTree(unittest.TestCase):
    def convert_naukri_tree(self, input_str: str):
        res = []
        input_list = input_str.split(' ')
        print('input_list', input_list)
        for el in input_list:
            el = int(el)
            if el == -1:
                res += [None]
            else:
                res += [el]
        return binarytree.build(res)
    
    def test_1(self):
        root = self.convert_naukri_tree('1 1 1 1 1 1 2 -1 -1 -1 -1 1 -1 2 2 -1 -1 -1 -1 -1 -1')
        print('root')
        print(root.pprint())
        expected = 8
        actual = countUnivalTrees(root)
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main()