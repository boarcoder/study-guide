'''
https://www.youtube.com/watch?v=vQBybrutCCY&t=14s
[M]
W and H, where W is work and H is holiday. Longest possible vacation given pto days off?

Option 1: Sliding window

W H H W W H W
  ----- pto window, store PTO_USED
if hit the max pto used, L += 1, R += 1 and re-calculate, as we never want a smaller window
moving forward, so the window never gets smaller. only if pto > 1 we extend window.
'''
def longestOnes_first_variant_1004_python(days: list[str], pto: int) -> int:
    if pto > len(days) or len(days) < pto:
        return len(days)
    WORK, HOLIDAY = 'W', 'H'
    L = 0
    R = 0
    rem_pto = pto
    max_vacation = min(len(days), pto)
    while R < len(days):
        if days[R] == WORK:
            rem_pto -= 1
        while rem_pto < 0 and L < R:
            if days[L] == WORK:
                rem_pto += 1
            L += 1
        max_vacation = max(max_vacation, R - L + 1)
        R += 1
    return max_vacation


if __name__ == '__main__':
    days = ['W', 'H', 'H', 'W', 'W', 'H', 'W']
    pto = 2
    assert longestOnes_first_variant_1004_python(days, pto) == 5

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 0
    assert longestOnes_first_variant_1004_python(days, pto) == 2

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 5
    print(longestOnes_first_variant_1004_python(days, pto))
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 10
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['H', 'H', 'H', 'H', 'H', 'H', 'H']
    pto = 0
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['W', 'H', 'W', 'W', 'W', 'H', 'W', 'H']
    pto = 1
    assert longestOnes_first_variant_1004_python(days, pto) == 3
