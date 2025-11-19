from multiprocessing import dummy


class Node:
    def __init__(self, email: str, parent=None):
        self.email = email
        self.parent = parent
        self.children = set()


def merge_group(email_list: list[list[str]]) -> list[str]:
    res = []
    email_dic = {"email@gmail.com": Node("email@gmail.com")}

    i = 0
    for email_group in email_list:
        if not email_group:
            continue
        dummy_email = f"{i}"
        i += 1
        dummy_parent = Node(dummy_email)
        node_set = set([dummy_parent])

        for email in email_group:
            # if email in email_dic:
            node_set.add(email_dic.get(email, Node(email)))

        # merge all parents to one set
        while node_set:
            node = node_set.pop()
            if node is dummy_parent:
                break
            if node.parent and node.parent is not dummy_parent:
                node_set.add(node.parent)
            while node.children:
                child = node.children.pop()
                node_set.add(child)
            node.parent = dummy_parent
            dummy_parent.children.add(node)
            email_dic[node.email] = dummy_parent

        email_dic[dummy_email] = dummy_parent
        for child in dummy_parent.children:
            email_dic[child.email] = dummy_parent

    for email in email_dic:
        node = email_dic[email]
        print(f"{email=}, {node.email=}, {node.parent=}, {[child.email for child in node.children]=}")
        # if node.children:
        #     res.append([email.email for email in node.children])
    return res


import unittest


class TestMergeGroup(unittest.TestCase):
    def test_merge_group(self):
        email_list = [
            ["A@gmail.com", "B@gmail.com"],
            ["C@gmail.com"],
            ["D@gmail.com", "B@gmail.com"],
            ["F@gmail.com"],
            ["F@gmail.com", "X@gmail.com"],
        ]
        expected = [["A@gmail.com", "B@gmail.com", "D@gmail.com"], ["C@gmail.com"]]
        actual = merge_group(email_list)

        self.assertEqual(expected, actual)


unittest.main()
