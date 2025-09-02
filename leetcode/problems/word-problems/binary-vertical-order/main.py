'''
[M] https://leetcode.ca/2016-10-09-314-Binary-Tree-Vertical-Order-Traversal/


Options: 
BFS and only return those in correct column
DFS and only return those in correct column
I will do BFS.
'''

from dataclasses import dataclass
import binarytree
from binarytree import Node
from collections import deque, defaultdict

@dataclass
class QueElement:
    node: Node
    column: int
        
class Solution:
    # def __init__(self):
    #     self.lowest_node = None

    def vertical_order(self, root: Node):
        col_dic = defaultdict(list)

        que = deque()
        que.appendleft(QueElement(root, 0))

        while que:
            node, col = que.popleft()
            if not node:
                continue
            col_dic[col] += [node.val]
            que.append(QueElement(node.left, col - 1))
            que.append(QueElement(node.right, col + 1))

        return [
            col_dic[col] for col in col
        ]


import unittest

class TestBinaryTree(unittest.TestCase):
    # def dfs(self, root, nodeval):
    #     if root is None:
    #         return None
    #     if root.val == nodeval:
    #         return root
    #     return self.dfs(root.left, nodeval) or self.dfs(root.right, nodeval)
    
    def test_1(self):
        root = binarytree.build(
            [3,9,20,None,None,15,7]
            )
        expected = [[9],[3,15],[20],[7]]
        s = Solution()
        actual = s.vertical_order(root)
        self.assertListEqual(expected, actual)

    def test_2(self):
        root = binarytree.build(
            [3,9,20,None,None,15,7]
            )
        expected = [[9],[3,15],[20],[7]]
        s = Solution()
        actual = s.vertical_order(root)
        self.assertListEqual(expected, actual)

    def test_3(self):
        root = binarytree.build(
            [3,9,8,4,0,1,7]
            )
        expected = [[4],[9],[3,0,1],[8],[7]]
        s = Solution()
        actual = s.vertical_order(root)
        self.assertListEqual(expected, actual)

        
if __name__ == '__main__':
    print('run tetts')
    unittest.main()
