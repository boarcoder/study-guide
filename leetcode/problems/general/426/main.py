"""
426
---
You are given the root of a Binary Search Tree (BST) and need to convert it into a sorted Circular Doubly-Linked List.
The conversion must be done in-place, meaning you should modify the existing tree nodes rather than creating new ones.

In the conversion:

The left pointer of each node should point to its predecessor (the previous node in sorted order)
The right pointer of each node should point to its successor (the next node in sorted order)
The list should be circular, meaning:
The right pointer of the last element should point to the first element
The left pointer of the first element should point to the last element
The BST property ensures that an in-order traversal gives us nodes in sorted order. After the transformation,
you should return a pointer to the smallest element (the head) of the resulting circular doubly-linked list.

For example, if you have a BST with values that would be [1, 2, 3, 4, 5] in sorted order, after conversion:

Node 1's left points to Node 5 (circular connection) and right points to Node 2
Node 2's left points to Node 1 and right points to Node 3
Node 3's left points to Node 2 and right points to Node 4
Node 4's left points to Node 3 and right points to Node 5
Node 5's left points to Node 4 and right points to Node 1 (circular connection)
If the input root is None, return None.

(tail)----> (head) [node.parent] [node] (tail)--->

            3
         2     4
      1           5

      1. dummy node (DUMMY)
      2. DFS left to the lowest value
      3.  (DUMMY)->(LOWEST LEFT)
      4. Set (DNODE).
        (DUMMY)->(LEFT 1st + DNODE)
      5. Return up, (DNODE) set the right to that. (DUMMY)->(LEFT 1st)->(LEFT 2nd + DNODE)
"""

import binarytree

example_tree = binarytree.bst(2, False, False)
print(f"{example_tree}")

"""

   42

   dummy <-> 42 
            dnode

"""

"""
https://leetcode.ca/all/426.html
TC: O(n)
SC: O(1)
M: [FAIL] 1:15:00
"""


class Solution:
    def __init__(self):
        self.dummy = binarytree.Node(-1, None, None)
        self.dnode = self.dummy

    def convert_bin_tree_dll(self, root: binarytree.Node):
        if not root:
            return None
        self.dfs(root)
        tail = self.dnode
        self.dnode.right = self.dummy.right
        self.dummy.right.left = tail
        return self.dummy.right

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.dnode.right = node
        node.left = self.dnode
        self.dnode = node
        self.dfs(node.right)
        return None
