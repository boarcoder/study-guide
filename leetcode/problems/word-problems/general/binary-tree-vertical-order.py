r"""
TC: O(n), w * log(w)+ n. still O(n) as w < n
SC: O(n). w + n still O(n) as w < n

lintcode:
Given a binary tree, return the vertical order traversal of its nodes' values. 
(ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Given binary tree {3,9,20,#,#,15,7}

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Return its vertical order traversal as:
[[9],[3,15],[20],[7]]

Given binary tree {3,9,8,4,0,1,7}

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
Return its vertical order traversal as:
[[4],[9],[3,0,1],[8],[7]]
"""

from binarytree import build


class Solution:
    def vertical_traverse(self, root):
        memo = {}
        bin_tree = root
        self.dfs(bin_tree, 0, memo)

        res = []
        # W log W
        print("memo", memo)
        for p in sorted(memo.keys()):
            res.append(memo[p])

        return res

    def dfs(self, node, position=0, memo={}):
        # we start at 0 as middle. left creates a -1 position. right +1 position.
        # at the end, we can place each node print into the proper column.
        if not node:
            return None

        if not memo.get(position, False):
            memo[position] = []
        memo[position].append(node.value)
        self.dfs(node.left, position - 1, memo)
        self.dfs(node.right, position + 1, memo)
        return None


s = Solution()
input_list = [3, 9, 20, None, None, 15, 7]
input_tree = build(input_list)
expected = [[9], [3, 15], [20], [7]]
actual = s.vertical_traverse(input_tree)
print("input_tree", input_tree)
print(f"""
expected: {expected}
actual: {actual}

""")

input_list = [3, 9, 8, 4, 0, 1, 7]
input_tree = build(input_list)
expected = [[4], [9], [3, 0, 1], [8], [7]]
actual = s.vertical_traverse(input_tree)
print("input_tree", input_tree)
print(f"""
expected: {expected}
actual: {actual}

""")
