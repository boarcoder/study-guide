"""
https://algo.monster/liteproblems/1868
Ref: M
TC: O(n) where n is the total numbers when decoded
SC: O(max(n,m)) encoded product list will be longer input list.
"""


class Solution:
    def findRLEArray(self, encoded1: list, encoded2: list) -> list:
        encoded1, encoded2 = (
            (encoded1, encoded2)
            if len(encoded1) > len(encoded2)
            else (encoded2, encoded1)
        )
        product_list = []

        i1 = -1
        i2 = -1
        times1 = 0
        times2 = 0
        while i1 < len(encoded1):
            num1, i1, times1 = self._encoded_next(encoded1, times1, i1)
            if num1 is None:
                break
            num2, i2, times2 = self._encoded_next(encoded2, times2, i2)
            if num2 is None:
                break
            product = num1 * num2
            self._encode_next_prod(product_list, product)
        return product_list

    def _encode_next_prod(self, encoded_list, num):
        prev_num = encoded_list[-1][0] if encoded_list else None
        if num == prev_num:
            # increase times + 1
            encoded_list[-1][1] += 1
        else:
            # add new elem
            encoded_list += [[num, 1]]

    def _encoded_next(self, encoded_list, remaining_times, i):
        if remaining_times == 0:
            i += 1
            if i >= len(encoded_list):
                return None, -1, 0
            remaining_times = encoded_list[i][1]
        # each tuple provides (num, times)
        num = encoded_list[i][0]
        remaining_times -= 1
        return num, i, remaining_times

    def encode(self, decoded_list):
        res = []
        prev_num = None
        times = 0
        for num in decoded_list + [0]:
            if num != prev_num:
                for i in range(times):
                    res += [prev_num]
                times = 0
                prev_num = num
            times += 1
        return res

    def decode(self, encoded_list):
        res = []
        for el in encoded_list:
            num, times = el
            for _ in range(times):
                res += [num]
        return res
