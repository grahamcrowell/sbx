from __future__ import annotations

import json
from itertools import chain
from typing import *

import pytest
from dotenv import load_dotenv

load_dotenv('.env')

EMPTY = 0
OK = 1
BAD = 2

def find_rotten(grid):
    out = []
    for r, col in enumerate(grid):
        for c in range(len(grid[r])):
            if grid[r][c] == BAD:
                out.append((r,c))
    return out

def solve(grid, t = 0):
    n = len(grid)
    m = len(grid[0])
    bads = find_rotten(grid)
    next_pos = []
    for bad in bads:
        br, bc = bad
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            r, c = br + dr, bc + dc
            if r < 0 or r >= n or c < 0 or c >= m:
                continue
            elif grid[r][c] == OK:
                next_pos.append((r, c))
    if next_pos:
        for r, c in next_pos:
            grid[r][c] = BAD
        t += 1
        return solve(grid, t)
    else:
        non_rotten_cnt = list(filter(lambda g: g == OK, chain(*grid)))
        print(non_rotten_cnt)
        if non_rotten_cnt:
            return -1
        return t


def _solve(grid, t, prev_non_rotten_cnt=0):
    non_rotten_cnt = list(filter(map(lambda g: g != BAD, chain(*grid))))
    if non_rotten_cnt != prev_non_rotten_cnt:
        return _solve(grid, t + 1, non_rotten_cnt)
    if non_rotten_cnt:
        return grid


def test():
    x = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expected = 4
    assert expected == solve(x)

def test_1():
    x = [[2,1,1],[0,1,1],[1,0,1]]
    expected = -1
    assert expected == solve(x)

def test_2():
    x = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expected = 4
    assert expected == solve(x)