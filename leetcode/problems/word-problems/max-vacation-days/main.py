"""
Calculate the maximum vacation days
There is a calendar array containing only "W" and "H".
W represents workdays, H represents holidays.
Given the number of paid time off (PTO) days, calculate the maximum consecutive vacation days.

For example, calendar=[W, W, H, W, W, H, W], PTO=3, longest_vacation=5
"""

HOLIDAY = "H"
WORKDAY = "W"


class Solution:
    def max_vacation_days(self, calendar: list, pto: int):
        L = 0
        R = 0

        max_len = 0
        remain = pto
        while R < len(calendar):
            if calendar[R] == WORKDAY:
                remain -= 1

            while remain < 0 and L < R:
                if calendar[L] == WORKDAY:
                    remain += 1
                L += 1
            if remain >= 0:
                if R - L + 1 > max_len:
                    # print(f"max len at {L=} {R=}: {R - L + 1}")
                    max_len = max(max_len, R - L + 1)
            R += 1
        return max_len
