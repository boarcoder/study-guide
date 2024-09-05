"""
TC:
SC:

"""


class Node:
    def __init__(self, key=None, freq=1, prev=None, _next=None):
        self.dic = {}
        if key is not None:
            self.dic[key] = True
        self.freq = freq
        self.prev = prev
        self.next = _next

    def pop_key(self, key):
        res = self.dic.get(key, "")
        if res:
            del self.dic[key]
        return res


class DLL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.freq_node_dic = {}
        self.key_freq_dic = {}

    def pop_node(self, node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
        return node

    def pop_key_from_node(self, node, key):
        res = node.pop_key(key)
        if not node.dic:
            self.pop_node(node)
        return res

    def increment_freq(self, key):
        node = self._get_node_by_key(key)
        self.insert_next_node(node, key)
        self.pop_key_from_node(node, key)

    def decrement_freq(self, key):
        node = self._get_node_by_key(key)
        self.insert_prev_node(node, key)
        self.pop_key_from_node(node, key)

    def get_min(self):
        return next(iter(self.tail.prev.keys())) if self.tail.prev is not None else ""

    def get_max(self):
        return (
            next(iter(self.head.next.dic.keys())) if self.head.next is not None else ""
        )

    def insert_next_node(self, node, key=None):
        freq = node.freq + 1
        if not self.freq_node_dic.get(freq, False):
            self.freq_node_dic[freq] = Node(key, freq, node, node.next)
        if key is not None:
            self.key_freq_dic[key] = self.freq_node_dic[freq]
        return self.freq_node_dic[freq]

    def insert_prev_node(self, node, key=None):
        freq = node.freq - 1
        if not self.freq_node_dic.get(freq, False):
            self.freq_node_dic[freq] = Node(key, freq, node.prev, node)
        if key is not None:
            if freq != 0:
                self.key_freq_dic[key] = self.freq_node_dic[freq]
        return self.freq_node_dic[freq]

    def _get_node_by_key(self, key):
        freq = self.key_freq_dic.get(key, False)
        if not freq:
            freq = 0
        return self.freq_node_dic.get(freq, False)

    def _get_node_by_freq(self, freq):
        return self.freq_node_dic.get(freq, False)


class AllInOne:
    def __init__(self):
        head = Node(0, 0, None, None)
        tail = Node(0, 0, head, None)
        head.next = tail
        self.dll = DLL(head, tail)

    def increment_key(self, key):
        """
        Increment by 1, or add new key with 1 freq.
        """
        self.dll.increment_freq(key)

    def decrement_key(self, key):
        """
        Decrement by 1, or remove a key if it has 1 freq. Do nothing if no key present.
        """
        self.dll.decrement_freq(key)

    def get_max_key(self):
        return self.dll.get_max()

    def get_min_key(self):
        return self.dll.get_min()


class AllOne:
    def __init__(self):
        head = Node(0, 0, None, None)
        tail = Node(0, 0, head, None)
        head.next = tail
        self.dll = DLL(head, tail)

    def inc(self, key):
        """
        Increment by 1, or add new key with 1 freq.
        """
        self.dll.increment_freq(key)

    def dec(self, key):
        """
        Decrement by 1, or remove a key if it has 1 freq. Do nothing if no key present.
        """
        self.dll.decrement_freq(key)

    def getMaxKey(self):
        return self.dll.get_max()

    def getMinKey(self):
        return self.dll.get_min()
