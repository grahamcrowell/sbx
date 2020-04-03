from typing import *
from math import factorial
from itertools import permutations


def perm(s: str):
    out = set()
    if len(s) == 2:
        return {s[1] + s[0], s[0] + s[1]}

    for i, y in enumerate(s):
        x = s[i]
        temp = list(
            map(lambda permetated: x + permetated, perm(s[:i] + s[i + 1:])))
        out = out.union(temp)
        if len(out) == factorial(len(s)):
            break
    return out


import pytest


@pytest.mark.parametrize('s', [('abc')])
def test2(s):
    assert len(perm(s)) == factorial(len(s))


@pytest.mark.parametrize('s', [('abc'), ('abcd'), ('abcde')])
def test1(s):
    assert perm(s) == set(map(lambda tup: ''.join(tup), set(permutations(s))))