r"""
LeetCode Problem: Flatten Binary Tree to Linked List

Goal: Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer 
  points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
- After flattening, all nodes should be connected via their right pointers, 
  with all left pointers set to None.

Example:
Input:
        1
       / \
      2   5
     / \   \
    3   4   6

Output (all nodes connected via right pointer):
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
"""

from typing import Optional
import unittest
from binarytree import Node, build


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.dnode = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        dummy = Node(0, None, None)
        self.dnode = dummy

        self.dfs(root)
        return dummy.right
        # self.flatten(root.left)

    def dfs(self, node):
        if not node:
            return None
        
        left = node.left
        right = node.right
        
        self.dnode.right = node
        self.dnode = self.dnode.right
        self.dnode.left = None
        self.dnode.right = None
        self.dfs(left)
        self.dfs(right)


# def tree_to_list(root):
#     """Helper function to convert flattened tree to list for verification."""
#     result = []
#     current = root
#     while current:
#         result.append(current.val)
#         if current.left:  # Should be None after flattening
#             raise ValueError("Left pointer should be None after flattening")
#         current = current.right
#     return result


class TestFlattenTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        r"""Test with the main example from the problem.
        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
        """
        # Create tree: [1, 2, 5, 3, 4, None, 6]
        root = build([1, 2, 5, 3, 4, None, 6])
        print('before')
        root.pprint()
        actual = self.solution.flatten(root)
        print('actual')
        actual.pprint()
        
        # Instead of trying to create a complex build array, let's verify the structure
        # by checking that each node is connected via its right pointer and all left pointers are None
        current = actual
        expected_values = [1, 2, 3, 4, 5, 6]
        
        for expected_val in expected_values:
            self.assertEqual(current.value, expected_val)
            self.assertIsNone(current.left)
            current = current.right
            
        # Verify the last node has no children
        self.assertIsNone(current)
    
    def test_single_node(self):
        """Test with a single node."""
        root = build([1])
        actual = self.solution.flatten(root)
        
        # Verify the single node structure
        self.assertEqual(actual.value, 1)
        self.assertIsNone(actual.left)
        self.assertIsNone(actual.right)
    


if __name__ == "__main__":
    # Run the tests
    print("Running tests...")
    unittest.main(argv=[""], exit=False, verbosity=2)
