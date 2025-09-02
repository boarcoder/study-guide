'''
1644. Lowest Common Ancestor of a Binary Tree II
https://leetcode.ca/all/1644.html
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, 
p and q. If either node p or q does not exist in the tree, return null. 
All values of the nodes in the tree are unique.

Solution:

    . (1, 2)
 .    . (2)
. 1  . 2

I will store a value to the fastest found parent of L/R N1/N2 nodes
Since it is DFS, the first time I set that value, it is LCA.
'''

import binarytree
from binarytree import Node

class Solution:
    def __init__(self):
        self.lowest_node = None

    def lowest_common_ancestor(self, root: Node, n1: Node, n2: Node):
        self.dfs(root, n1, n2)
        return self.lowest_node

    def dfs(self, node, n1, n2):
        if self.lowest_node:
            return self.lowest_node
        if node is None:
            return None
        L = self.dfs(node.left, n1, n2)
        R = self.dfs(node.right, n1, n2)

        if L in [n1, n2] and R in [n1, n2]:
            self.lowest_node = node
            return None
        return L or R
        

import unittest

class TestBinaryTree(unittest.TestCase):
    def dfs(self, root, nodeval):
        if root is None:
            return None
        if root.val == nodeval:
            return root
        return self.dfs(root.left, nodeval) or self.dfs(root.right, nodeval)
    
    def test_1(self):
        root = binarytree.build(
            [3,5,1,6,2,0,8,None,None,7,4]
            )
        p = self.dfs(root, 5)
        q = self.dfs(root, 1)
        expected = 3
        s = Solution()
        actual = s.lowest_common_ancestor(root, p, q)


    def test_2(self):
        root = binarytree.build(
            [3,5,1,6,2,0,8,None,None,7,4]
        )
        p = self.dfs(root, 5)
        q = self.dfs(root, 4)
        expected = 5
        s = Solution()
        actual = s.lowest_common_ancestor(root, p, q)
        

    def test_3(self):
        root = binarytree.build(
            [3,5,1,6,2,0,8,None,None,7,4]
        )
        p = self.dfs(root, 5)
        q = Node(10)
        expected = None
        s = Solution()
        actual = s.lowest_common_ancestor(root, p, q)
        
if __name__ == '__main__':
    print('run tetts')
    unittest.main()
