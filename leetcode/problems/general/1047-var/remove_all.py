'''
1047. https://www.youtube.com/watch?v=wdKnnXw9cfU
[M] FAIL 32 min
If the letter is adjacent to itself, remove all of it
If the letter is duplicated elsewhere, only remove the duplication
TC:O(n)
SC:O(n)
'''
def remove_all_adjacent_duplicates_variant_1047_python(s):
    res = ''
    stack = []
    for i in range(len(s)):
        if stack and stack[-1]['ch'] != s[i]:
            if stack[-1]['ct'] > 1:
                stack.pop()
        if stack and stack[-1]['ch'] == s[i]:
            stack[-1]['ct'] += 1
        else:
            stack.append(
                {'ch': s[i], 'ct': 1}
            )
    if stack and stack[-1]['ct'] > 1:
        stack.pop()
    res = ''
    for el in stack:
        res += el['ch']
    print('res', res)
    return res

if __name__ == '__main__':
    s = "azxxxzy"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ay"

    s = "abbaxx"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabbccdd"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aaabbaad"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "d"

    s = "abcdefg"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "abcdefg"

    s = "abbcddeff"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "ace"

    s = "abcdeffedcba"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == ""

    s = "aabccddeeffbbbbbbbbbf"
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "f"

    s = "abbbacca"; # Cannot pick and choose duplicates in the middle to delete first
    assert remove_all_adjacent_duplicates_variant_1047_python(s) == "a"
