import heapq
from collections import deque


def lex_str(input_str):
    heap = []
    que = deque()
    ch_ct_dic = {}
    tmp = []
    for ch in input_str:
        ch_ct_dic[ch] = ch_ct_dic.get(ch, 0) + 1

    for ch in ch_ct_dic:
        freq = ch_ct_dic[ch]
        if freq % 2 != 0:
            tmp.append(ch * freq)
            continue
        heapq.heappush(heap, (-ord(ch), freq, ch))

    if tmp:
        que.append(tmp[0])
    while heap:
        order, freq, ch = heapq.heappop(heap)
        if freq == 1:
            tmp.append(ch)
            continue
        for i in range(0, freq, 2):
            que.appendleft(ch)
            que.append(ch)

    res = ""
    for el in que:
        res += el

    return res


input_str = "yxxy"
expected = "xyyx"
actual = lex_str(input_str)
print(f"""
expected: {expected}
actual: {actual}
      """)


input_str = "babab"
expected = "abbba"
actual = lex_str(input_str)
print(f"""
expected: {expected}
actual: {actual}
      """)
