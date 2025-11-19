"""
Stream of data, parse json, every input token is a number.

1:"test", 2:"text2"

if u see repeated input, not interpretable.
such as duplicate key exception

Different order, not sorted.

REturn the previous text on a duplicate key.

REmove all special characters
"""

import json


class Solution:
    def __init__(self):
        self.dic = {i: "asdf" for i in range(100)}
        self.dup = 50
        self.dic[self.dup] = "the duplicated key first val"
        self.json_str = json.dumps(self.dic)[:-1] + f', "{self.dup}": "duplicate keys val"' + r"}"
        self.iterator = iter(self.json_str)

        self.builder_open = False
        self.builder_str = ""
        self.builder_int = 0
        print(self.json_str)

    def stream_data_tokens(self):
        seen = {}
        key, val = None, None
        while True:
            try:
                token = self.get_next_token()
                print("got token:", token)
            except:
                return False
            # print(f"{token=}{key=}{val=}|{self.builder_str=}|{self.builder_int=}")
            res, item_type = self.lex(token)
            if item_type == "INT":
                key = res
            elif item_type == "STRING":
                val = res
                # print("seen:", seen)
                # print("cur key: ", key)
                if seen.get(key, False):
                    return seen[key]
                seen[key] = val
                key, val = None, None
        return False

    def get_next_token(self):
        return next(self.iterator)

    def lex(self, ch: str):
        if ch in "0123456789":
            if self.builder_int is None:
                self.builder_int = 0
            self.builder_int = self.builder_int * 10 + int(ch)
            if self.builder_str:
                res_str = self.builder_str
                self.builder_str = ""
                return res_str, "STRING"
        elif ch == r'"':
            if self.builder_open:
                res = self.builder_str
                self.builder_str = ""
                self.builder_open = False
                return res, "STRING"
            elif self.builder_int is not None:
                res = self.builder_int
                self.builder_int = None
                return res, "INT"
            else:
                self.builder_open = True
        elif ch not in "{}', ":
            self.builder_str += ch
            return None, "NONE"
        return None, "NONE"


if __name__ == "__main__":
    s = Solution()
    answer = s.stream_data_tokens()
    print(f"{answer=}")
