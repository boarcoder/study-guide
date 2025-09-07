r"""
Given a binary tree, assume there are 2 people
each on one side of the tree.

Return the values of the binary tree nodes
that both people can see. Return in one list[int]

Order should be:
left side, bottom to top
right side, top to bottom.

Returns: [4, 2, 1, 1, 3, 7]

               1
              / \
             2   3
            / \ / \
           4  5 6  7

# CLARIFYING QUESTION

> When we say both see, do we mean if both people don't see the node, don't add?
NO. EACH PERSON will add the nodes that they can see. 
> Do we need to dedup the nodes?
You do not have to deduplicate. Each person can add the nodes that they see.

# OPTION 1

BFS where we store min,max node val per level.
- Every level, we can then take L (min) R (max) for those to add to res

# OPTION 2

DFS where we pass up per level the avail value. We will accept min(L) max(R) to pass up,
and then once all are collected, we add that for the level in a arr or level dict.

"""

import unittest
from binarytree import Node
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class QueElement:
    node: Node
    distance: int
    depth: int


class Solution:
    def both_sides_binary_tree(self, tree: Node):
        mins = defaultdict(lambda: float("inf"))
        maxes = defaultdict(lambda: float("-inf"))
        res = defaultdict(lambda: [None, None])
        que = [QueElement(tree, 0, 0)]
        while que:
            elem = que.pop()
            if not elem.node:
                continue
            if elem.distance < mins[elem.depth]:
                mins[elem.depth] = min(mins[elem.depth], elem.distance)
                res[elem.depth][0] = elem.node.val
            if elem.distance > maxes[elem.depth]:
                maxes[elem.depth] = max(maxes[elem.depth], elem.distance)
                res[elem.depth][1] = elem.node.val
            que.append(QueElement(elem.node.left, elem.distance - 1, elem.depth + 1))
            que.append(QueElement(elem.node.right, elem.distance + 1, elem.depth + 1))

        return [res[i][0] for i in reversed(res)] + [res[i][1] for i in res]


class TestBothSidesBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test with None/empty tree - should return empty list"""
        result = self.solution.both_sides_binary_tree(None)
        self.assertEqual(result, [])

    def test_single_node(self):
        """Test with single node - both people see it, so it appears twice"""
        root = Node(5)
        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [5, 5])

    def test_complete_binary_tree(self):
        r"""
        Test with complete binary tree:
               1
              / \
             2   3
            / \ / \
           4  5 6  7
        
        Left side (bottom to top): 4, 2, 1
        Right side (top to bottom): 1, 3, 7
        Expected: [4, 2, 1, 1, 3, 7] (1 appears twice as root is seen by both)
        """
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [4, 2, 1, 1, 3, 7])

    def test_left_skewed_tree(self):
        r"""
          Test with left-skewed tree:
              1
             /
            2
           /
          3
         /
        4

          Left side (bottom to top): 4, 3, 2, 1
          Right side (top to bottom): 1, 2, 3, 4
          Expected: [4, 3, 2, 1, 1, 2, 3, 4] (each level has same node on both sides)
        """
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [4, 3, 2, 1, 1, 2, 3, 4])

    def test_right_skewed_tree(self):
        r"""
        Test with right-skewed tree:
        1
         \
          2
           \
            3
             \
              4
        
        Left side (bottom to top): 1, 2, 3, 4
        Right side (top to bottom): 1, 2, 3, 4
        Expected: [4, 3, 2, 1, 1, 2, 3, 4] (each level has same node on both sides)
        """
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [4, 3, 2, 1, 1, 2, 3, 4])

    def test_unbalanced_tree(self):
        r"""
        Test with unbalanced tree:
              10
             /  \
            5    20
           / \     \
          3   7    25
         /   / 
        1   6   
        
        Left side (bottom to top): 1, 3, 5, 10
        Right side (top to bottom): 10, 20, 25, 6]
        Expected: [1, 3, 5, 10, 10, 20, 25, 6]] (10 appears twice as root is seen by both)
        """
        root = Node(10)
        root.left = Node(5)
        root.right = Node(20)
        root.left.left = Node(3)
        root.left.right = Node(7)
        root.right.right = Node(25)
        root.left.left.left = Node(1)
        root.left.right.left = Node(6)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [1, 3, 5, 10, 10, 20, 25, 6])

    def test_complex_tree(self):
        r"""
        Test with complex tree structure:
                 1
               /   \
              2     3
             / \     \
            4   5     6
               / \   / \
              7   8 9   10
             /           \
            11           12
        
        Left side (bottom to top): 11, 4, 2, 1
        Right side (top to bottom): 1, 3, 6, 10, 12
        Expected: [11, 7, 4, 2, 1, 1, 3, 6, 10, 12] (1 appears twice as root is seen by both)
        """
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.right = Node(6)
        root.left.right.left = Node(7)
        root.left.right.right = Node(8)
        root.right.right.left = Node(9)
        root.right.right.right = Node(10)
        root.left.right.left.left = Node(11)
        root.right.right.right.right = Node(12)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [11, 7, 4, 2, 1, 1, 3, 6, 10, 12])

    def test_tree_with_gaps(self):
        r"""
        Test tree with missing nodes at various levels:
              15
             /  \
            10   20
           /      \
          5       30
           \     /
            8   25
        
        Left side (bottom to top): 8, 5, 10, 15
        Right side (top to bottom): 15, 20, 30, 25
        Expected: [8, 5, 10, 15, 15, 20, 30, 25] (15 appears twice as root is seen by both)
        """
        root = Node(15)
        root.left = Node(10)
        root.right = Node(20)
        root.left.left = Node(5)
        root.right.right = Node(30)
        root.left.left.right = Node(8)
        root.right.right.left = Node(25)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [8, 5, 10, 15, 15, 20, 30, 25])

    def test_two_level_tree(self):
        r"""
        Test simple two-level tree:
            1
           / \
          2   3
        
        Left side (bottom to top): 2, 1
        Right side (top to bottom): 1, 3
        Expected: [2, 1, 1, 3] (1 appears twice as root is seen by both)
        """
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [2, 1, 1, 3])

    def test_zigzag_tree(self):
        r"""
        Test tree with zigzag pattern:
            1
           /
          2
           \
            3
           /
          4
           \
            5
        
        Left side (bottom to top): 5, 4, 3, 2, 1
        Right side (top to bottom): 1, 2, 3, 4, 5
        Expected: [5, 4, 3, 2, 1, 1, 2, 3, 4, 5] (duplicates allowed for nodes seen by both)
        """
        root = Node(1)
        root.left = Node(2)
        root.left.right = Node(3)
        root.left.right.left = Node(4)
        root.left.right.left.right = Node(5)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [5, 4, 3, 2, 1, 1, 2, 3, 4, 5])

    def test_tree_with_negative_values(self):
        r"""
        Test tree with negative values:
             0
            / \
          -5   5
          /   / \
        -10  3   8
        
        Left side (bottom to top): -10, -5, 0
        Right side (top to bottom): 0, 5, 8
        Expected: [-10, -5, 0, 0, 5, 8] (0 appears twice as root is seen by both)
        """
        root = Node(0)
        root.left = Node(-5)
        root.right = Node(5)
        root.left.left = Node(-10)
        root.right.left = Node(3)
        root.right.right = Node(8)

        result = self.solution.both_sides_binary_tree(root)
        self.assertEqual(result, [-10, -5, 0, 0, 5, 8])


if __name__ == "__main__":
    unittest.main()
