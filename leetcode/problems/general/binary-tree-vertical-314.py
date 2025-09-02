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
        # tree = build(root)
        dic = {}
        self.dfs(root, 0, 0, dic)
        print("dic", dic)
        return self.dic_to_list(dic)

    def dic_to_list(self, dic):
        res = []
        for key in sorted(dic.keys()):
            res.append(dic[key])
        return res

    def dfs(self, node, distance, level, dic):
        if not node:
            return None

        dic[distance] = dic.get(distance, []) + [node.val]
        self.dfs(node.left, distance - 1, level + 1, dic)
        self.dfs(node.right, distance + 1, level + 1, dic)


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
