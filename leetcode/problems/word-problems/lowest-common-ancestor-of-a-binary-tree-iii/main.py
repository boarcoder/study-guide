'''
lowest-common-ancestor-of-a-binary-tree-iii (LC Prem)
https://www.naukri.com/code360/problems/lowest-common-ancestor-of-a-binary-tree-iii_1280134?leftPanelTabValue=SUBMISSION
[M]
Given nodes with parent reference

1. We could take node1, and store every parent in a dict. 
TC: O(h) SC: O(h)

2. Can we avoid storing in a dict?
You can iterate to calculate each node's depth first.
A node parent has to be at lower depth, so that determines who gets to move up first.
TC: O(h) SC: O(1)
'''

from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:

class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def get_depth(node):
    depth = 0
    while node.parent:
        node = node.parent
        depth += 1
    return depth

def lowestCommonAncestor(n1, n2):
    node1, node2 = n1, n2
    depth1, depth2 = get_depth(node1), get_depth(node2)
    # root node will always be returned if both depths are 0.
    while depth1 >= 0 and depth2 >= 0:
        if node1 == node2:
            return node1
        if depth1 > depth2:
            node1 = node1.parent
            depth1 -= 1
        else:
            node2 = node2.parent
            depth2 -= 1

    return None