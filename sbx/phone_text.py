from __future__ import annotations

import json
from copy import copy
from typing import *

import pytest
from dotenv import load_dotenv

load_dotenv('.env')


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'i'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        out = []

        def back(combo, rem_digits):
            if not rem_digits:
                out.append(combo)
            else:
                for letter in phone[rem_digits[0]]:
                    back(combo + letter, rem_digits[1:])
            

        if digits:
            back("", digits)
        return out


@pytest.mark.parametrize('digits, expected', [
    ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
])
def test_dial(digits, expected):
    s = Solution()
    combo = s.letterCombinations(digits)
    assert combo == expected
