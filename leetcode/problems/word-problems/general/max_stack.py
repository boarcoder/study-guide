"""
TC:
SC:
Max Stack:
top() must call in O(1)
any other function must call in O(log(n))

Approach 1:
- O(n) spc stack stores order and O(1) top
- O(n) spc heap stores max - we must store the location of a DLL node to effectively pop.

"""

from typing import Optional
import heapq


class Node:
    def __init__(self, val=None, prev=None, _next=None):
        self.val = val
        self.prev = prev
        self.next = _next


class DLL:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.min_heap = []

    def push(self, x):
        node = Node(val=x, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = node
        heapq.heappush(self.min_heap, (-x, node))

    def pop(self):
        if self.tail.prev is not self.head:
            node = self.tail.prev
            before_node = node.prev
            before_node.next = node.next
            return node.val
        else:
            return None

    def pop_node(self, node):
        before_node = node.prev
        after_node = node.next
        before_node.next = after_node
        after_node.prev = before_node
        return node

    def top(self):
        # how do i remove from the heap ??
        if self.tail.prev is not self.head:
            return self.tail.prev.val
        return None

    def peek_max(self):
        if not self.min_heap:
            return None
        return -self.min_heap[-1][0]

    def pop_max(self):
        # get node from minheap
        neg_val, node = heapq.heappop(self.min_heap)
        self.pop_node(node)
        return -neg_val


class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def peek_max(self):
        pass

    def pop_max(self):
        pass
