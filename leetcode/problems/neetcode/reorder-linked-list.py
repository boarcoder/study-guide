"""
TC: O(n)
SC: O(1)
https://neetcode.io/problems/reorder-linked-list
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_len = self.get_list_len(head)
        d1, d2 = self.split_list(head, list_len)
        d2 = self.reverse_linked_list(d2.next)
        node = head
        revnode = d2
        while node:
            tmp = node.next
            if revnode:
                if node.next == revnode:
                    return
                node.next = revnode
                revnode = revnode.next
                node = node.next
                node.next = tmp
            node = tmp

    def get_list_len(self, head):
        i = 0
        node = head
        while node:
            i += 1
            node = node.next
        return i

    def split_list(self, head, list_len):
        d1 = ListNode(None, None)
        d2 = ListNode(None, None)
        node1 = d1
        node2 = d2
        node = head
        i = 0
        while node:
            tmp = node.next
            if i < list_len // 2 and node1:
                node1.next = node
                node1 = node1.next
            elif node2:
                node2.next = node
                node2 = node2.next
            node = tmp
            i += 1
        return d1, d2

    def reverse_linked_list(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev
