r"""
TC: O(n)
SC: O(1) for search
O(n) for parentize

[M]
LCA 3
--
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1
"""

from binarytree import build, get_parent


class Solution:
    def lca(self, root, p, q):
        # add parents to binarytree for problem
        self._parentize(root)
        p = self.dfs_val(root, p)
        q = self.dfs_val(root, q)

        # find parent that is common
        a, b = p, q
        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p
        else:
            return a

    def _parentize(self, node, parent=None):
        if not node:
            return None
        node.parent = parent
        self._parentize(node.left, node)
        self._parentize(node.right, node)
        return node

    def dfs_val(self, node, val):
        if not node:
            return False
        if node.value == val:
            return node
        L = self.dfs_val(node.left, val)
        R = self.dfs_val(node.right, val)
        return L or R


s = Solution()
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
tree = build(root)
expected = s.dfs_val(tree, 3)
actual = s.lca(tree, p, q)
print("tree", tree, p, q)
print(f"""
expected: {expected}
actual: {actual}
""")

s = Solution()
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 1
tree = build(root)
expected = s.dfs_val(tree, 3)
actual = s.lca(tree, p, q)
print("tree", tree, p, q)
print(f"""
expected: {expected}
actual: {actual}
""")


s = Solution()
root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
p = 5
q = 4
tree = build(root)
expected = s.dfs_val(tree, 5)
actual = s.lca(tree, p, q)
print("tree", tree, p, q)
print(f"""
expected: {expected}
actual: {actual}
""")
