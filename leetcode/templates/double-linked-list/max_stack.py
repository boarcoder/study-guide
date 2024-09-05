"""
TC: O(log(n)) max ops
SC: O(n)
[L]
-Must do O(1) on top
-Must do O(log(n)) on max
https://www.lintcode.com/problem/859
"""

from sortedcontainers import SortedList
from typing import Optional


class Node:
    def __init__(self, value=None, _prev=None, _next=None):
        self.value = value
        self.prev = _prev
        self.next = _next


class DLL:
    def __init__(self):
        self.head: Optional[Node] = Node("head", None, None)
        self.tail: Optional[Node] = Node("tail", self.head, None)
        self.head.next = self.tail

    def unlink(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        return node

    def insert_value_end(self, value):
        before_node = self.tail.prev
        after_node = self.tail
        node = Node(value, before_node, self.tail)
        before_node.next = node
        after_node.prev = node
        return node


class MaxStack:
    def __init__(self):
        self.dll = DLL()
        self.sorted_list = SortedList(key=lambda x: x.value)

    def push(self, x: int):
        # O(log(n)) where n scales stack length.
        node = self.dll.insert_value_end(x)
        self.sorted_list.add(node)

    def pop(self):
        # O(log(n)) where n scales stack length.
        if self.dll.tail.prev != self.dll.head:
            node = self.dll.unlink(self.dll.tail.prev)
            self.sorted_list.remove(node)
            return node.value
        raise Exception("MaxStack is empty")

    def top(self):
        # O(1)
        if self.dll.tail.prev != self.dll.head:
            return self.dll.tail.prev.value
        raise Exception("MaxStack is empty")

    def peekMax(self):
        # O(1)
        if not self.sorted_list:
            raise Exception("MaxStack is empty, there is no max")
        return self.sorted_list[-1].value

    def popMax(self):
        # O(log(n)) where n scales stack length.
        if not self.sorted_list:
            raise Exception("MaxStack is empty, there is no max")
        node = self.sorted_list.pop()
        self.dll.unlink(node)
        return node.value
