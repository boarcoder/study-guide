"""
TC:
SC:

"""

from typing import Optional


class Node:
    def __init__(self, freq, _prev, _next):
        self.freq = freq
        self.key_set = set()
        self.prev: Optional[Node] = _prev
        self.next: Optional[Node] = _next

    def pn(self):
        return {
            "f": self.freq,
            "nx": self.next.freq if self.next is not None else "o",
            "pv": self.prev.freq if self.prev is not None else "o",
            "key_set": self.key_set,
        }


class DLL:
    def __init__(self):
        self.head = Node(0, None, None)
        self.tail = Node(float("inf"), self.head, None)
        self.head.next = self.tail
        self.key_node_dic = {}

    def prints(self):
        res = []
        node = self.head
        while node:
            res.append(node.pn())
            node = node.next
        print(res)

    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None

    def _clean_node(self, node, key):
        if key in node.key_set:
            node.key_set.remove(key)
        if not node.key_set and node.freq != 0:
            self.unlink(node)

    def _get_existing_node(self, key):
        if key in self.key_node_dic:
            return self.key_node_dic[key]
        else:
            return False

    def increment_key(self, key):
        node = self._get_existing_node(key)
        if not node:
            node = self.head
        freq = node.freq + 1
        if node.next.freq != freq:
            node.next = Node(freq, node, node.next)
            node.next.next.prev = node.next
        node.next.key_set.add(key)
        self.key_node_dic[key] = node.next
        self._clean_node(node, key)

    def decrement_key(self, key):
        node = self._get_existing_node(key)
        if not node:
            return None
        freq = node.freq - 1
        if node.prev.freq != freq:
            node.prev = Node(freq, node.prev, node)
            node.prev.prev.next = node.prev
        if node.prev.freq != 0:
            node.prev.key_set.add(key)
        self.key_node_dic[key] = node.prev
        self._clean_node(node, key)

    def get_max_key(self):
        node = self.tail.prev
        key_set = node.key_set
        return next(iter(key_set)) if key_set else ""

    def get_min_key(self):
        node = self.head.next
        key_set = node.key_set
        return next(iter(key_set)) if key_set else ""


AllOne = DLL
AllOne.inc = DLL.increment_key
AllOne.dec = DLL.decrement_key
AllOne.getMaxKey = DLL.get_max_key
AllOne.getMinKey = DLL.get_min_key
