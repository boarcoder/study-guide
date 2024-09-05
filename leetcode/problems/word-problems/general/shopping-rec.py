"""
TC: O( (P * I^2) + (C * log(I)) )
Adjacency list
P previous orders
I avg items per order
C items in current customer order

SC:  O((P * I^2) + C)
----
[A]
Given customer_list, store_order_history,
a new customer buys something‍‌‌‌‍‍‍‍‍‍‍‍‍‍‍‍ in customer_list.

Recommend the most relevant recommended items.
Based on store_order_history - which is a list
of previous order_list
"""

import heapq


def recommend_items(customer_list, store_order_history):
    # We need to build a relevance based on store_order_history first
    graph = {}
    for order_list in store_order_history:
        for item in order_list:
            graph[item] = {}
            for elem in order_list:
                if elem != item:
                    # negative for max-heap effect on heapq minheap.
                    graph[item][elem] = graph[item].get(elem, 0) - 1

    for item in graph:
        graph[item]["heap"] = graph[item].get("heap", [])
        print("graph[item]", graph[item])
        for related_item in graph[item]:
            if related_item == "heap":
                continue
            graph[item]["heap"].append((graph[item][related_item], related_item))
        print('graph[item]["heap"]', graph[item]["heap"])
        heapq.heapify(graph[item]["heap"])
    # the result is a count of every item also in same order, applied to each key
    # incremented if it happened in more than 1 order.
    # space complexity is O(I * S) where I=Items, S=average order size of items list

    # We collect what is going to be relevant and select the top n.
    relevant_items_dic = {}
    for item in customer_list:
        if not graph.get(item, False):
            # theres nothing related.
            continue
        # assume only 1st relevant item
        k = 1
        for _ in range(k):
            relevant = graph[item]["heap"][0]
            relevant_item = relevant[1]
            relevant_items_dic[relevant_item] = (
                relevant_items_dic.get(relevant_item, 0) + 1
            )
    return relevant_items_dic


customer_list = ["grape", "blueberry", "clock", "pineapple", "folder", "pen", "pencil"]
store_order_history = [["grape", "clock"], ["pineapple", "grape"]]
print(f"""
expected: ?
actual: {recommend_items(customer_list, store_order_history)}
""")
