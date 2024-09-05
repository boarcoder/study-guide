import unittest

"""
Requirement:
Push O(1)
Pop O(1)
Top O(1)
Rest: Optimal as possible

self.max_stack:
[
    (
        element that is max at i in self.stack, 
        i of element
    )
]
Such that:
We can go to i of a popped max element, and mark as deleted
We can mark everything after i as new max that was previous to this.
"""


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.max_stack_len = 0
        # self.heap = []

    def push(self, element):
        self.stack.append(element)
        self.max_stack.append(max(element, self.max_stack[-1]))
        self.max_stack_len += 1

    def pop(self):
        element = self.max_stack.pop()
        self.max_stack_len -= 1
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1][0]

    def popMax(self):
        self.max_stack_len -= 1
        if self.max_stack_len < 0:
            return None
        element, i = self.max_stack[self.max_stack_len]
        # the end boundary of max stack is where this element was at.
        self.max_stack_len = i


class TestMaxStack(unittest.TestCase):
    def setUp(self):
        self.stack = MaxStack()

    def test_push_and_top(self):
        self.stack.push(5)
        self.assertEqual(self.stack.top(), 5)
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)

    def test_pop(self):
        self.stack.push(3)
        self.stack.push(2)
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 3)
        self.assertIsNone(self.stack.pop())

    def test_peekMax(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peekMax(), 3)
        self.stack.push(5)
        self.assertEqual(self.stack.peekMax(), 5)
        self.stack.push(2)
        self.assertEqual(self.stack.peekMax(), 5)

    def test_popMax(self):
        self.stack.push(5)
        self.stack.push(1)
        self.stack.push(5)
        self.assertEqual(self.stack.popMax(), 5)
        self.assertEqual(self.stack.top(), 1)
        self.assertEqual(self.stack.popMax(), 5)
        self.assertEqual(self.stack.top(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.pop())

    def test_empty_stack(self):
        self.assertIsNone(self.stack.top())
        self.assertIsNone(self.stack.peekMax())
        self.assertIsNone(self.stack.pop())
        self.assertIsNone(self.stack.popMax())

    def test_multiple_operations(self):
        self.stack.push(5)
        self.stack.push(1)
        self.assertEqual(self.stack.popMax(), 5)
        self.stack.push(5)
        self.assertEqual(self.stack.top(), 5)
        self.assertEqual(self.stack.popMax(), 5)
        self.assertEqual(self.stack.peekMax(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.top())


if __name__ == "__main__":
    unittest.main()
