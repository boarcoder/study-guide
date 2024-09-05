import unittest
import binarytree

r"""
TC: 
SC: 
[L] Leaves of binary tree
https://leetcode.ca/all/366.html

Given a binary tree, collect a tree's nodes as if you were doing this: 
Collect and remove all leaves, repeat until the tree is empty.
Example:
Input: [1,2,3,4,5]
 
          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]

bfs_que:
[
    (1, None, 0)
    (2, 1-ref, 1)
    (3, 1-ref, 1)
    (4, 2-ref, 2)
    (5, 2-ref, 2)
]

tree_dic:
{
    1: DEPTH after 1 (+2),
    2: DEPTH after 2: (+1),
    4: DEPTH after 4: (+0),
}
"""


class Solution:
    def __init__(self):
        self.leaf_dic = {}

    def leaves_of_binary_tree(self, root):
        # dfs down and trace the depth after node, to calc the leafiness
        self.dfs(root)
        return list(self.leaf_dic.values())

    def dfs(self, node):
        if not node:
            return 0

        L, R = 0, 0
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        following_depth = max(L, R) + 1
        self.leaf_dic[following_depth] = self.leaf_dic.get(following_depth, [])
        self.leaf_dic[following_depth].append(node.value)
        return following_depth


class TestLeavesBinary(unittest.TestCase):
    def test_leaves_binary_1(self):
        input_list = [1, 2, 3, 4, 5]
        input_tree = binarytree.build(input_list)

        expected = [[4, 5, 3], [2], [1]]
        s = Solution()
        actual = s.leaves_of_binary_tree(input_tree)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
