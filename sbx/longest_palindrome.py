from typing import *

import pytest


def is_pali(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def expandPalindrome(s: str, start: int, end: int):
    print(f"expanding=s[{start}:{end}]={s[start:end]}")
    assert s[start:end] == s[start:end][-1::-1]
    while start > 0 and end < len(s):
        if s[start - 1] == s[end]:
            start -= 1
            end += 1
        else:
            break
    return s[start:end]


def longestPalindrome(s: str) -> str:
    print(f"longestPalindrome({s})")
    # mid start
    # start = len(s) // 2
    # end = start + 1
    init_pos = []
    current_length = 1
    current_palindrome = s[0]
    for i in range(len(s)):
        if i + 3 < len(s) and s[i] == s[i + 2]:
            init_pos.append((i, i + 3))
        if i + 2 < len(s) and s[i] == s[i + 1]:
            init_pos.append((i, i + 2))
    print(f"init_pos={init_pos}")
    for start, end in init_pos:
        palindrome = expandPalindrome(s, start, end)
        print(f"expanded to: {palindrome}")

        if len(palindrome) > current_length:
            print(f"new longest: {palindrome}")
            current_length = len(palindrome)
            current_palindrome = palindrome
    return current_palindrome


# aabad
# a => ok init, add 1
# aa => ok, add 1
# aab => no, add another
# aaba => no, remove 0th
# aba => ok
# abad => no
# aabad => no
@pytest.mark.parametrize('arg, expected', [
    ("babad", "bab"),
    ("aabad", "aba"),
])  # yapf: disable
def test(arg, expected):
    x = list(range(10))
    assert longestPalindrome(arg) == expected