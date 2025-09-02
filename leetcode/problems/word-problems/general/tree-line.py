import binarytree
from collections import deque


def tree_line(root: binarytree.Node):
    que = deque()
    que.appendleft((root, 0))
    line_i = 0
    while que:
        node, h = que.popleft()
        if h > line_i:
            line_i = h
            print()
        print(node.value, end=" ")
        if node.left:
            que.append((node.left, h + 1))
        if node.right:
            que.append((node.right, h + 1))
    print("\n---------------")
    root.pprint()


def get_example_tree():
    return binarytree._build_bst_from_sorted_values([0, 1, 2, 3, 4, 5, 6])


tree_line(get_example_tree())
