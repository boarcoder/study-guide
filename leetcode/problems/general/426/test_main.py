"""
Unit tests for the convert_bin_tree_dll function.
Tests the conversion of a Binary Search Tree to a sorted Circular Doubly-Linked List.
"""

import os
import sys
import unittest
from binarytree import Node, bst, build

# Add the current directory to sys.path to import main.py
sys.path.insert(0, os.path.dirname(__file__))

# Import or define the Solution class
# Assuming the Solution class will contain the convert_bin_tree_dll method
try:
    from main import Solution
except ImportError:
    # If Solution class doesn't exist yet, create a mock one for testing
    class Solution:
        def convert_bin_tree_dll(self, root):
            # This will be replaced by the actual implementation
            from main import convert_bin_tree_dll

            return convert_bin_tree_dll(root)


class TestConvertBSTtoDLL(unittest.TestCase):
    """Test cases for converting BST to Circular Doubly-Linked List."""

    def setUp(self):
        """Initialize a Solution instance for each test."""
        # Create a new Solution instance for each test to avoid state pollution
        # since the Solution class doesn't properly reset its dummy/dnode state
        pass

    # Helper methods for verification
    def _safe_traverse_dll(self, head, max_iterations=1000):
        """Safely traverse a circular DLL with loop detection.
        Returns a list of (node, value) tuples or None if traversal fails.
        """
        if head is None:
            return []

        nodes = []
        current = head
        visited = set()
        iterations = 0

        while iterations < max_iterations:
            # Check if we've seen this node before (not at the start)
            if id(current) in visited:
                # We've completed the circle back to a visited node
                if current is head:
                    # Proper circular list
                    break
                else:
                    # Malformed list - circular but not back to head
                    break

            visited.add(id(current))
            nodes.append((current, current.val))

            # Check if we have a next node
            if current.right is None:
                # End of list (not circular)
                break

            current = current.right
            iterations += 1

            # Check if we've returned to the head (proper circular list)
            if current is head:
                break

        return nodes

    def verify_dll_structure(self, head):
        """Verify that the DLL structure is correct (each node's left points to prev, right to next)."""
        if head is None:
            return True

        current = head
        visited = set()
        max_iterations = 1000
        iterations = 0

        while iterations < max_iterations:
            # Check for infinite loops
            if id(current) in visited:
                # If we're back at the head, that's expected for circular
                if current is head and iterations > 0:
                    break
                # Otherwise, we have a malformed cycle
                if current is not head:
                    return False
            visited.add(id(current))

            # Verify bidirectional links
            # Use 'is not None' to avoid triggering binarytree's __bool__ which causes infinite loop
            if current.right is not None:
                if current.right.left is not current:
                    return False
            if current.left is not None:
                if current.left.right is not current:
                    return False

            # Move to next node
            if current.right is None:
                # End of list - not circular yet
                break

            current = current.right
            iterations += 1

            if current is head:
                break

        return True

    def verify_circular_connections(self, head):
        """Verify that the list is properly circular."""
        if head is None:
            return True

        # Check if head has proper left/right pointers
        if not hasattr(head, "left") or not hasattr(head, "right"):
            return False

        # Find the tail by traversing forward with safety
        nodes = self._safe_traverse_dll(head)
        if not nodes:
            return False

        # Get the last node in the traversal
        tail = nodes[-1][0] if nodes else None

        if tail is None:
            return False

        # Verify circular connections
        # The tail's right should point to head
        # The head's left should point to tail
        try:
            # Use 'is' instead of '==' to avoid triggering binarytree's __eq__
            return tail.right is head and head.left is tail
        except AttributeError:
            return False

    def verify_sorted_order(self, head):
        """Verify that values are in ascending order."""
        if head is None:
            return True

        values = self.extract_values_from_dll(head)
        return values == sorted(values)

    def extract_values_from_dll(self, head):
        """Extract all values from the circular DLL in order."""
        if head is None:
            return []

        nodes = self._safe_traverse_dll(head)
        return [value for node, value in nodes]

    def count_nodes_in_dll(self, head):
        """Count the total number of nodes in the circular DLL."""
        if head is None:
            return 0

        nodes = self._safe_traverse_dll(head)
        return len(nodes)

    def get_all_tree_nodes(self, root):
        """Get all node objects from a binary tree."""
        if root is None:
            return set()

        nodes = set()
        stack = [root]

        while stack:
            node = stack.pop()
            nodes.add(id(node))
            # Use 'is not None' check to avoid triggering binarytree's __bool__
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return nodes

    # Edge case tests
    def test_none_tree(self):
        """Test with None input, should return None."""
        solution = Solution()  # Create fresh instance
        result = solution.convert_bin_tree_dll(None)
        self.assertIsNone(result)

    def test_single_node(self):
        """Test single node BST - should point to itself circularly."""
        root = Node(42)
        solution = Solution()  # Create fresh instance
        head = solution.convert_bin_tree_dll(root)

        self.assertIsNotNone(head)
        self.assertEqual(head.val, 42)
        # Use 'is' instead of '==' to avoid triggering binarytree's __eq__ which causes infinite loop
        self.assertIs(head.left, head)  # Points to itself (circular)
        self.assertIs(head.right, head)  # Points to itself (circular)
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))

    def test_two_nodes_left_child(self):
        """Test two nodes with left child configuration."""
        # Tree structure: 2
        #                /
        #               1
        root = Node(2)
        root.left = Node(1)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_two_nodes_right_child(self):
        """Test two nodes with right child configuration."""
        # Tree structure: 1
        #                  \
        #                   2
        root = Node(1)
        root.right = Node(2)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    # Basic BST conversion tests
    def test_three_node_balanced(self):
        """Test balanced tree with 3 nodes."""
        # Tree structure:   2
        #                  / \
        #                 1   3
        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_five_node_balanced(self):
        """Test balanced tree with 5 nodes."""
        # Tree structure:     3
        #                   /   \
        #                  2     5
        #                 /     /
        #                1     4
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        root.right = Node(5)
        root.right.left = Node(4)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_complete_binary_tree(self):
        """Test complete binary tree."""
        # Using binarytree to build: values [4, 2, 6, 1, 3, 5, 7]
        #         4
        #       /   \
        #      2     6
        #     / \   / \
        #    1   3 5   7
        values = [4, 2, 6, 1, 3, 5, 7]
        root = build(values)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))
        self.assertEqual(self.count_nodes_in_dll(head), 7)

    def test_perfect_binary_tree(self):
        """Test perfect binary tree with all levels filled."""
        # Perfect BST with 15 nodes
        values = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        root = build(values)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        expected = list(range(1, 16))
        self.assertEqual(self.extract_values_from_dll(head), expected)
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))
        self.assertEqual(self.count_nodes_in_dll(head), 15)

    # Unbalanced tree tests
    def test_left_skewed_tree(self):
        """Test tree with only left children (linked list shape)."""
        # Tree structure: 5
        #                /
        #               4
        #              /
        #             3
        #            /
        #           2
        #          /
        #         1
        root = Node(5)
        root.left = Node(4)
        root.left.left = Node(3)
        root.left.left.left = Node(2)
        root.left.left.left.left = Node(1)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_right_skewed_tree(self):
        """Test tree with only right children."""
        # Tree structure: 1
        #                  \
        #                   2
        #                    \
        #                     3
        #                      \
        #                       4
        #                        \
        #                         5
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        root.right.right.right = Node(4)
        root.right.right.right.right = Node(5)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_zigzag_tree(self):
        """Test alternating left-right children pattern."""
        # Tree structure:   5
        #                  /
        #                 2
        #                / \
        #               1   3
        #                    \
        #                     4
        root = Node(5)
        root.left = Node(2)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.left.right.right = Node(4)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_heavily_unbalanced(self):
        """Test tree with significant imbalance."""
        # Tree structure:     10
        #                    /  \
        #                   5    15
        #                  /      \
        #                 2       20
        #                / \       \
        #               1   3      25
        #                    \
        #                     4
        root = Node(10)
        root.left = Node(5)
        root.left.left = Node(2)
        root.left.left.left = Node(1)
        root.left.left.right = Node(3)
        root.left.left.right.right = Node(4)
        root.right = Node(15)
        root.right.right = Node(20)
        root.right.right.right = Node(25)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(
            self.extract_values_from_dll(head), [1, 2, 3, 4, 5, 10, 15, 20, 25]
        )
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    # Trees with same values but different structures
    def test_same_values_different_structure_1(self):
        """Test first arrangement of values 1-5."""
        # Tree structure:     3
        #                   /   \
        #                  1     4
        #                   \     \
        #                    2     5
        root = Node(3)
        root.left = Node(1)
        root.left.right = Node(2)
        root.right = Node(4)
        root.right.right = Node(5)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_same_values_different_structure_2(self):
        """Test alternative arrangement of values 1-5."""
        # Tree structure:       4
        #                      /
        #                     2
        #                   /   \
        #                  1     3
        #                         \
        #                          5
        root = Node(4)
        root.left = Node(2)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right = Node(5)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [1, 2, 3, 4, 5])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    # Larger trees and complex scenarios
    def test_large_balanced_tree(self):
        """Test BST with 20+ nodes."""
        # Generate a random BST using binarytree
        tree = bst(height=4, is_perfect=False)

        # Store original values for comparison BEFORE conversion
        # Important: Must collect values before conversion to avoid circular reference issues
        original_values = sorted([node.val for node in tree.levelorder])

        solution = Solution()  # Create fresh instance
        head = solution.convert_bin_tree_dll(tree)

        if head is not None:  # Only check if tree was not empty - Use 'is not None' to avoid __bool__
            result_values = self.extract_values_from_dll(head)
            self.assertEqual(result_values, original_values)
            self.assertTrue(self.verify_dll_structure(head))
            self.assertTrue(self.verify_circular_connections(head))
            self.assertTrue(self.verify_sorted_order(head))

    def test_random_bst(self):
        """Test with randomly generated valid BST."""
        # Generate multiple random BSTs and test
        for _ in range(5):
            tree = bst(height=3)

            if tree is not None:  # Only test non-empty trees - Use 'is not None' to avoid __bool__
                # Store original values BEFORE conversion to avoid circular reference issues
                original_values = sorted([node.val for node in tree.levelorder])

                solution = Solution()  # Create fresh instance
                head = solution.convert_bin_tree_dll(tree)

                result_values = self.extract_values_from_dll(head)
                self.assertEqual(result_values, original_values)
                self.assertTrue(self.verify_dll_structure(head))
                self.assertTrue(self.verify_circular_connections(head))
                self.assertTrue(self.verify_sorted_order(head))

    def test_tree_with_negative_values(self):
        """Test BST containing negative numbers."""
        # Tree structure:     0
        #                   /   \
        #                 -5     10
        #                /  \   /
        #              -10  -2  5
        root = Node(0)
        root.left = Node(-5)
        root.left.left = Node(-10)
        root.left.right = Node(-2)
        root.right = Node(10)
        root.right.left = Node(5)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(self.extract_values_from_dll(head), [-10, -5, -2, 0, 5, 10])
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    def test_tree_with_large_values(self):
        """Test BST with large integer values."""
        # Tree structure with large values
        root = Node(1000000)
        root.left = Node(500000)
        root.left.left = Node(100000)
        root.right = Node(2000000)
        root.right.right = Node(3000000)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        self.assertEqual(
            self.extract_values_from_dll(head),
            [100000, 500000, 1000000, 2000000, 3000000],
        )
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))

    # In-place modification verification
    def test_in_place_modification(self):
        """Verify that the conversion is done in-place (reuses original nodes)."""
        # Create a tree and store references to all nodes
        root = Node(4)
        node2 = Node(2)
        node6 = Node(6)
        node1 = Node(1)
        node3 = Node(3)
        node5 = Node(5)
        node7 = Node(7)

        root.left = node2
        root.right = node6
        node2.left = node1
        node2.right = node3
        node6.left = node5
        node6.right = node7

        # Store original node IDs
        original_node_ids = {
            id(root),
            id(node2),
            id(node6),
            id(node1),
            id(node3),
            id(node5),
            id(node7),
        }

        # Convert to DLL
        solution = Solution()  # Create fresh instance

        head = solution.convert_bin_tree_dll(root)

        # Collect all node IDs from the DLL
        dll_node_ids = set()
        if head is not None:  # Use 'is not None' to avoid triggering binarytree's __bool__
            current = head
            # Use a counter to prevent infinite loops
            max_iterations = 1000
            iterations = 0
            while iterations < max_iterations:
                dll_node_ids.add(id(current))
                current = current.right
                iterations += 1
                if current is head:
                    break

        # Verify same nodes are used (in-place modification)
        self.assertEqual(
            original_node_ids,
            dll_node_ids,
            "Conversion should reuse original nodes (in-place)",
        )
        self.assertEqual(
            len(dll_node_ids), 7, "All original nodes should be in the DLL"
        )

    def test_empty_bst_from_binarytree(self):
        """Test with an empty BST from binarytree."""
        # Create empty tree
        tree = None

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(tree)

        self.assertIsNone(head)

    def test_complex_asymmetric_tree(self):
        """Test complex asymmetric BST."""
        # Tree structure:        50
        #                      /    \
        #                    30      70
        #                   /  \    /  \
        #                  20  40  60  80
        #                 /   /  \    /  \
        #                10  35  45  75  90
        #                           /
        #                          72
        root = Node(50)
        root.left = Node(30)
        root.right = Node(70)
        root.left.left = Node(20)
        root.left.right = Node(40)
        root.right.left = Node(60)
        root.right.right = Node(80)
        root.left.left.left = Node(10)
        root.left.right.left = Node(35)
        root.left.right.right = Node(45)
        root.right.right.left = Node(75)
        root.right.right.right = Node(90)
        root.right.right.left.left = Node(72)

        solution = Solution()  # Create fresh instance


        head = solution.convert_bin_tree_dll(root)

        expected = [10, 20, 30, 35, 40, 45, 50, 60, 70, 72, 75, 80, 90]
        self.assertEqual(self.extract_values_from_dll(head), expected)
        self.assertTrue(self.verify_dll_structure(head))
        self.assertTrue(self.verify_circular_connections(head))
        self.assertTrue(self.verify_sorted_order(head))
        self.assertEqual(self.count_nodes_in_dll(head), 13)


if __name__ == "__main__":
    unittest.main()
