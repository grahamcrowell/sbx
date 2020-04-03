from __future__ import annotations

import json
from copy import copy
from queue import Queue
from typing import *

import pytest
from dotenv import load_dotenv

load_dotenv('.env')


class LRUCache:
    """https://leetcode.com/problems/lru-cache/"""
    def __init__(self, capacity: int):
        self.n = capacity
        self.data = {}
        self.order = 0
        self.used_at = {}
        self.rev_used_at = {}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        else:
            self.order += 1
            prev_order = self.used_at[key]
            del self.rev_used_at[prev_order]
            self.used_at[key] = self.order
            self.rev_used_at[self.order] = key
            return self.data[key]

    def _evict(self):
        evict_used_at = min(self.used_at.values())
        key = self.rev_used_at[evict_used_at]
        del self.used_at[key]
        del self.data[key]
        del self.rev_used_at[evict_used_at]

    def put(self, key: int, value: int):
        self.order += 1
        if key not in self.data and len(self.data) == self.n:
            self._evict()
        self.data[key] = value
        self.used_at[key] = self.order
        self.rev_used_at[self.order] = key


@pytest.mark.parametrize('params, expected', [
                        ([[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]],
                         [None, -1, None, -1, None, None, 2, 6])
                        ]) # yapf: disable
def test_harness(params, expected):
    n = params[0][0]
    cache = LRUCache(n)
    print(f"LRUCache({n})")
    param_expected = list(zip(params, expected))
    for param, expected in param_expected[1:]:
        if len(param) == 1:
            print(f"{expected} == get({param[0]}) = {cache.get(param[0])}")
            assert expected == cache.get(param[0])
        else:
            print(f"put({param[0]},{param[1]})")
            assert expected is None
            cache.put(param[0], param[1])


def test():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert 1 == cache.get(1)
    cache.put(3, 3)
    assert -1 == cache.get(2)
    cache.put(4, 4)
    assert -1 == cache.get(1)
    assert 3 == cache.get(3)
    assert 4 == cache.get(4)
