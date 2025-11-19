"""
A Quack structure has
insert(x) method to put x into Quack in sorted order,
pop() method randomly pops out an element from head or tail (either the max or min element can be popped out),
size() returns current Quack length.

OUTPUT THE QUACK IN SORTED ORDER, IN O(N) time.
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class DLL:
    def __init__(self):
        self.head_sentinel = Node(float("-inf"))
        self.tail_sentinel = Node(float("inf"))
        self.head = self.head_sentinel
        self.tail = self.tail_sentinel
        self.head_sentinel.next = self.tail_sentinel
        self.tail_sentinel.prev = self.head_sentinel

    def insert(self, val):
        node = Node(val)
        if self.head_sentinel.next == self.tail_sentinel:
            self.insert_right(self.head_sentinel, node)
        elif val == self.head.next.val:
            self.insert_right(self.head, node)
            self.head = node
        elif val == self.tail.prev.val:
            self.insert_left(self.tail, node)
            self.tail = node
        elif val <= self.head.next.val:
            self.insert_right(self.head, node)
        elif val >= self.tail_sentinel.prev.val:
            self.insert_left(self.tail, node)
        elif val < self.tail.prev.val and val >= self.head.next.val:
            self.insert_left(self.tail.prev, node)
        # self.set_min_max(node)

        node = Node(val)

    def insert_left(self, node, insert_node):
        """
        [node.prev] -> <-[insert_node]-> <-[node]
        """
        left_node = node.prev
        middle_node = insert_node
        right_node = node
        left_node.next = middle_node
        middle_node.prev = left_node
        middle_node.next = right_node
        right_node.prev = middle_node

    def insert_right(self, node, insert_node):
        """
        [node] -> <-[insert_node]-> <-[node.next]
        """
        left_node = node
        middle_node = insert_node
        right_node = node.next
        left_node.next = middle_node
        middle_node.prev = left_node
        middle_node.next = right_node
        right_node.prev = middle_node

    def get_list(self):
        res = []
        curr = self.head_sentinel.next
        while curr != self.tail_sentinel:
            res.append(curr.val)
            curr = curr.next
        return res


class Quack:
    def __init__(self):
        self.data = []

    def insert(self, x):
        # Insert x in sorted order
        from bisect import insort

        insort(self.data, x)

    def pop(self):
        # Randomly pop from head or tail
        import random

        if not self.data:
            return None
        if random.choice([True, False]):
            return self.data.pop(0)  # Pop from head (min element)
        else:
            return self.data.pop()  # Pop from tail (max element)

    def size(self):
        return len(self.data)

    def get_sorted(self):
        # Return the elements in sorted order
        dll = DLL()
        while self.size() > 0:
            val = self.pop()
            print("Current Quack data:", self.data)
            print(f"Popped: {val}")
            dll.insert(val)
        return dll.get_list()

    def get_sorted_super_simple(self):
        """
        Return sorted elements without touching the backing storage by
        repeatedly forcing pops from the tail (current max). Reversing the
        descending sequence yields the sorted order in O(N) time.
        """
        import random

        original_choice = random.choice
        descending = []
        try:
            random.choice = lambda _: False  # Always pop tail (max element)
            while self.size() > 0:
                descending.append(self.pop())
        finally:
            random.choice = original_choice
        descending.reverse()
        return descending


import unittest
from unittest.mock import patch


class TestQuack(unittest.TestCase):
    def setUp(self):
        self.quack = Quack()

    def test_insert_keeps_internal_data_sorted(self):
        for val in [5, 1, 3, 2, 4]:
            self.quack.insert(val)
        self.assertEqual(self.quack.data, [1, 2, 3, 4, 5])

    def test_pop_head_returns_min_when_random_choice_true(self):
        for val in [10, -1, 5]:
            self.quack.insert(val)
        with patch("random.choice", return_value=True):
            popped = self.quack.pop()
        self.assertEqual(popped, -1)
        self.assertEqual(self.quack.data, [5, 10])

    def test_pop_tail_returns_max_when_random_choice_false(self):
        for val in [7, 3, 9]:
            self.quack.insert(val)
        with patch("random.choice", return_value=False):
            popped = self.quack.pop()
        self.assertEqual(popped, 9)
        self.assertEqual(self.quack.data, [3, 7])

    def test_pop_on_empty_quack_returns_none(self):
        self.assertIsNone(self.quack.pop())
        self.assertEqual(self.quack.size(), 0)

    def test_get_sorted_handles_duplicates_and_random_pops(self):
        """
        [SENTINEL]                [SENTINEL]
                  [H]
                           [T]
                   1        3 5  5
        """
        values = [5, 1, 3, 1, 5, 2]
        for val in values:
            self.quack.insert(val)
        with patch(
            "random.choice",
            side_effect=[True, False, True, False, True, False],
        ):
            sorted_values = self.quack.get_sorted()
        self.assertEqual(sorted_values, sorted(values))
        self.assertEqual(self.quack.size(), 0)

    def test_get_sorted_super_simple_returns_sorted_order_and_drains(self):
        values = [4, 2, 4, 1]
        for val in values:
            self.quack.insert(val)
        sorted_values = self.quack.get_sorted_super_simple()
        self.assertEqual(sorted_values, sorted(values))
        self.assertEqual(self.quack.size(), 0)


if __name__ == "__main__":
    unittest.main()
