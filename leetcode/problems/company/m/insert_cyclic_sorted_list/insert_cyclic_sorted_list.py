"""
https://leetcode.ca/all/708.html
Ref: M
TC: O(N) insert worst case
SC: O(1) insert
"""


class Solution:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next if next else self


class Solution:
    def insert(self, node: ListNode, x: int):
        head = node
        node_insert = ListNode(x)
        node_insert.next = node_insert
        while node:
            if self._is_insert_node(node, x, head):
                self._insert_after(node, node_insert)
                return head
            node = node.next
        return head or node_insert

    def _is_insert_node(self, node: ListNode, x: int, head: ListNode):
        return any(
            (
                # usual scenario
                node.next.val >= x and node.val <= x,
                # what if node.next.val is HEAD?
                node.next.val <= node.val and node.val <= x,
                # what if this is a single loop?
                node.next == node,
                # what if this is the minimum value in the middle or end? [5, 7, 8, [[1]], 2, 3]
                all(
                    (
                        node.val >= node.next.val,
                        x <= node.val,
                        x <= node.next.val,
                    )
                ),
            )
        )

    def _insert_after(self, node: ListNode, node_insert: ListNode):
        tmp = node.next
        node.next = node_insert
        node_insert.next = tmp
