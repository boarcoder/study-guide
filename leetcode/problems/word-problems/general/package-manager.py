"""
AMZN word problem
* Design a package manager and installer. Each package has dependencies.

Input:
a -> b,c,d
b -> e,f,
----
Note: Could be done faster with a tree? No, but would be simpler for debug if
reader provide bad dependency list.
TC: O(n)
SC: O(n) - topo sort
"""

from collections import deque
from textwrap import dedent
import unittest


class PackageManager:
    def __init__(self, input_str):
        self.graph = self._get_graph(input_str)

    def install(self):
        if not self.graph:
            print("No dependencies to install")
            return []
        dependency_list = self._topo_sort(self.graph)
        # Here we would install each dep. But I just return the order of install.
        return dependency_list

    def _topo_sort(self, graph):
        # get the order required for an install. graph keys are parent.
        indegree_dic = {}
        for parent in graph:
            child_list = graph[parent]
            # the child requires +1 parent dependency before it can install
            for child in child_list:
                indegree_dic[child] = indegree_dic.get(child, 0) + 1
                # the parent requires at least 0 deps.
                indegree_dic[parent] = indegree_dic.get(parent, 0)

        order_list = []
        source_list = deque()
        for child in indegree_dic:
            if indegree_dic[child] == 0:
                source_list.append(child)

        if not source_list:
            raise Exception(
                "There are no source dependencies to install. Circular dependency detected"
            )

        while source_list:
            # may need a circular detection other than source_list?
            parent = source_list.popleft()
            order_list.append(parent)
            for child in graph[parent]:
                indegree_dic[child] -= 1
                if indegree_dic[child] == 0:
                    source_list.append(child)

        if len(order_list) != len(indegree_dic):
            raise Exception("Circular dependency or missing dependency detected")

        return order_list

    def _get_graph(self, input_str):
        graph = {}
        lines = input_str.split("\n")
        for line in lines:
            if "->" not in line:
                continue
            child, parent_list = line.split("->")
            child = child.strip()
            graph[child] = graph.get(child, [])
            for parent in parent_list.split(","):
                parent = parent.strip()
                graph[parent] = graph.get(parent, [])
                graph[parent].append(child)
        return graph


class TestPackageManager(unittest.TestCase):
    def test_installs_in_proper_order(self):
        input_str = dedent("""
        a -> b,c,d
        b -> e,f
        """)
        expected = [
            "c",
            "d",
            "e",
            "f",
            "b",
            "a",
        ]  # or e f b c d a, either works!
        pm = PackageManager(input_str)
        actual = pm.install()
        self.assertListEqual(expected, actual)

def fn(param):
    # i need to add carousel
    # i need image component
    # i need a arrow click handler
    


unittest.main()
