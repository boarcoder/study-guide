"""
Input: "Hello hello, hello world this is me and ME!"

- Find Top K frequent words.
- Optimize the code to give top K+10 or K+20 freq without doing repeated computations.
- Propose solution if the Priority queue cannot be stored locally beyond a certain limit.

AMZN
---
Note:
For cannot store heap locally, what should we do?
So in other words, we cannot store O(n) for n words in memory.
That is memory req. What to do?
1. We'd have to split the function call up into multiple calls on the datas.
Function calls f,
f = (n * WORD_MEM) / (TOTAL_MEMORY_AVAIL)
2. For any given list, we seek top k (assuming k fits in memory) - and write to disk.
3. Combine all list with top k, heapify, and then call function again.
>>> This is assuming we can fit in memory: K * [ (n * WORD_MEM) / (TOTAL_MEM) ]
Then our time complexity for this is still based on number of words total, but we multiply by f.
TC: O(n * f * log(k)), where f = (n * WORD_MEM) / (TOTAL_MEMORY_AVAIL)
SC: O(f + k)
"""

import textwrap
import heapq

alpha = "abcdefghijklmnopqrstuvqxyz"


def top_k_freq(input_str: str, k: int, memo={}):
    res = []
    if memo is not None and memo["heap"]:
        if k < len(memo["prev"]):
            return memo["prev"][k - 1]
        # if user requesting k past a given elem and we already calculated
        heap = memo["heap"]
        res += memo["prev"]
        for i in range(k - memo["cur"]):
            if not heap:
                break
            word = heapq.heappop(heap)[1]
            memo["prev"].append(word)
            res.append(word)
        return res

    heap = []
    word_dic = {}

    word = ""
    for ch in input_str:
        ch = ch.lower()
        if ch not in alpha:
            if word:
                word_dic[word] = word_dic.get(word, 0) + 1
                word = ""
        else:
            word += ch

    for word in word_dic:
        heap.append((-word_dic[word], word))
    heapq.heapify(heap)

    for i in range(k):
        if heap:
            res.append(heapq.heappop(heap)[1])
    # store cache
    memo["heap"] = heap.copy()
    memo["cur"] = i + 1
    memo["prev"] = res[:]
    return res


input_str = "Hello hello, world this is me and ME!"
k = 2
memo = {"cur": 0, "heap": [], "prev": []}
expected = ["hello", "me"]
output_str = textwrap.dedent(
    f"""
    should provide top k words for:
    k: {k}
    input_str: {input_str}

    EXPECTED: {expected}
    ACTUAL: {top_k_freq(input_str, k, memo)}
    """
)
print(output_str)


input_str = (
    "a a a a a a b b b c c d d e e f f g h i j k l m n o p qqq rrr sss ttt vvvv vv"
)
k = 2
memo = {"cur": 0, "heap": [], "prev": []}
expected = ["a", "b"]
output_str = textwrap.dedent(
    f"""
    should provide top k words for:
    k: {k}
    input_str: {input_str}

    EXPECTED: 
    [
        ['a', 'b'],
        ['a', 'b', 'c'],
        ['a', 'b', 'c', 'd', 'e'],
    ]
    ACTUAL: 
    [
        {top_k_freq(input_str, 2, memo)},
        {top_k_freq(input_str, 3, memo)},
        {top_k_freq(input_str, 4, memo)},
    ]
    """
)
print(output_str)
