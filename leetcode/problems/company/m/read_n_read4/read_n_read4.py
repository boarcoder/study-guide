"""
Link: https://www.lintcode.com/problem/660 https://leetcode.ca/all/158.html
Ref: Meta, Uber
TC: read: O(n)
SC: read: O(n)
n characters are written to return buffer
"""


class Solution:
    def __init__(self):
        self.read_buffer_len = 4
        self.read_buffer = [None] * self.read_buffer_len
        self.R = self.read_buffer_len
        self.W = 0

    def read(self, buf, n):
        self._reset_write_state(buf, n)
        i = 0
        while i < n:
            if self._is_end_of_read_buffer():
                self._update_read_buffer()
                continue
            if self._is_end_of_file():
                break
            self._update_write_buffer(buf)
            i += 1
        return i

    def _is_end_of_file(self):
        return self.read_buffer[self.R] is None

    def _is_end_of_read_buffer(self):
        return self.R >= self.read_buffer_len

    def _update_read_buffer(self):
        self.R = 0
        self.read_buffer = [None] * self.read_buffer_len
        Reader.read4(self.read_buffer)

    def _update_write_buffer(self, buf):
        buf[self.W] = self.read_buffer[self.R]
        self.R += 1
        self.W += 1

    def _reset_write_state(self, buf, n):
        buf = [] * n
        self.W = 0


test = "123456asd"
for i, ch in enumerate(test):
    print(i, ch)
