'''
LC 156 Prem
https://www.naukri.com/code360/problems/upside-down-binary-tree_1281853

Option 1: BFS

    __5
   /   \
  4     3
 / \
1   2

I open a BFS queue, and place each level into the que.

[ 
    (5, 0),
    (4, 1), (3, 1), 
    (1, 2), (2, 2),
]

I then go to the back of the queue.

If I did BFS with Right to left, then it would go
1-2 -> 

 d
    1

2-2

 d
    1
       

'''
import binarytree
from binarytree import Node

class Solution:
    def __init__(self):
        # hold a class level reference to node we are constructing from
        self.dnode = None

    def dfs(self, node):
        if node is None:
            return None
        
        if node.left:
            L = self.dfs(node.left)
            self.dnode.right = L
            node.left = None
            # self.dnode = self.dnode.right

        if node.right:
            R = self.dfs(node.right,)
            self.dnode.left = R
            node.right = None

        if self.dnode.right:
            self.dnode = self.dnode.right
        return node

    def flipTree(self, root):
        dummy = Node(0)
        self.dnode = dummy
        dummy_root = Node(0)
        dummy_root.left = root
        self.dfs(dummy_root)
        return dummy.right

import unittest

class TestBinaryTree(unittest.TestCase):    
    def test_1(self):
        s = Solution()
        root = binarytree.build(
            [5, 4, 3, 1, 2, None, None, None, None, None, None]
            )
        expected = binarytree.build(
            [1, 2, 4, None, None, 3, 5]
        )
        print('root input')
        print(root.pprint())
        print('>>>>>>>>>>>>>>>>>>')
        print('expect')
        print(expected.pprint())
        print('>>>>>>>>>>>>>>>>>>')
        actual = s.flipTree(root)
        print('actual')
        print(actual.pprint())
        print('>>>>>>>>>>>>>>>>>>')
        self.assertEqual(expected.pprint(), actual.pprint())
        
if __name__ == '__main__':
    print('run tetts')
    unittest.main()