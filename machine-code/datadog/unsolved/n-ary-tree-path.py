'''
"n-ray tree max path sum from root to leaf"
class TreeNode:
def __init__(self, score):
"""
Initializes an n-ary tree node.
:param score: The score of the node """
self.score = score # Value of the node
self.children = [ ] # List to store child nodes
def max_root_to_leaf_sum(root):
"""
Calculates the maximum path sum from the root node to a leaf node.
:param root: TreeNode, the root node of the tree
:return: int, the maximum path sum """
if not root: # Returns 0 directly for an empty node
return 0
if not root.children: # If it is a leaf node, directly return the value of the current node
return root.score
Recursively calculate the maximum path sum of all child nodes and take the maximum value
max_child_sum = max(max_root_to_leaf_sum(child) for child in root.children)
Return the value of the current node plus the maximum path sum of its subtree
return root.score + max_child_sum
Notes:
The problem is asking to find the maximum path sum from the root to a leaf node in an N-ary tree.
A related problem is LeetCode 124 "Binary Tree Maximum Path Sum" 
. However, LeetCode 124 finds the maximum path sum between any two nodes, not just from root to leaf.
'''