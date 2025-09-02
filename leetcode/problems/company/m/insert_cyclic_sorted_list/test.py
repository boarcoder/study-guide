import unittest
from insert_cyclic_sorted_list import Solution


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next if next else self


def create_circular_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    prev = head
    for val in values[1:]:
        node = Node(val)
        prev.next = node
        prev = node
    prev.next = head
    return head


def linked_list_to_list(head: "Node") -> list:
    if not head:
        return []
    result = []
    current = head
    while True:
        result.append(current.val)
        current = current.next
        if current == head:
            break
    return result


s = Solution()
insert = s.insert


class TestInsertIntoCircularLinkedList(unittest.TestCase):
    def test_example1(self):
        head = create_circular_linked_list([3, 4, 1])
        insertVal = 2
        new_head = insert(head, insertVal)
        expected = [3, 4, 1, 2]
        actual = linked_list_to_list(new_head)
        print("actual:", linked_list_to_list(new_head))
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_example2(self):
        head = create_circular_linked_list([])
        insertVal = 1
        new_head = insert(head, insertVal)
        expected = [1]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_example3(self):
        head = create_circular_linked_list([1])
        insertVal = 0
        new_head = insert(head, insertVal)
        expected = [1, 0]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_insert_minimum(self):
        head = create_circular_linked_list([2, 3, 4, 5])
        insertVal = 1
        new_head = insert(head, insertVal)
        expected = [2, 3, 4, 5, 1]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_insert_minimum_2(self):
        head = create_circular_linked_list([5, 7, 8, 2, 3])
        insertVal = 1
        new_head = insert(head, insertVal)
        expected = [5, 7, 8, 1, 2, 3]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_insert_maximum(self):
        head = create_circular_linked_list([1, 2, 3, 4])
        insertVal = 5
        new_head = insert(head, insertVal)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_insert_maximum_in_middle(self):
        head = create_circular_linked_list([1, 2, 1])
        insertVal = 3
        new_head = insert(head, insertVal)
        expected = [1, 2, 3, 1]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_insert_duplicate(self):
        head = create_circular_linked_list([1, 2, 2, 3])
        insertVal = 2
        new_head = insert(head, insertVal)
        expected = [1, 2, 2, 2, 3]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_all_same_values(self):
        head = create_circular_linked_list([2, 2, 2])
        insertVal = 2
        new_head = insert(head, insertVal)
        expected = [2, 2, 2, 2]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_single_element_insert_larger(self):
        head = create_circular_linked_list([1])
        insertVal = 2
        new_head = insert(head, insertVal)
        expected = [1, 2]
        self.assertEqual(expected, linked_list_to_list(new_head))

    def test_single_element_insert_smaller(self):
        head = create_circular_linked_list([1])
        insertVal = 0
        new_head = insert(head, insertVal)
        expected = [1, 0]
        self.assertEqual(expected, linked_list_to_list(new_head))


unittest.main()
