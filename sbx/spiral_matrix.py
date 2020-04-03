from pprint import pprint
from typing import *

import pytest


def set(r, c, x, grid):
    print(f"set({r}, {c}, {x}, grid)")
    OK = True
    OK *= r < len(grid)
    OK *= c < len(grid[0])
    OK *= r >= 0
    OK *= c >= 0

    OK = bool(OK)
    if OK and grid[r][c] is None:
        grid[r][c] = x
        return True
    return False


def show(grid, r, c, x):
    print(r, c, x)
    for row in grid:
        print(row)


def solve(n, r=0, c=0, x=1, grid=None):
    if grid is None:
        grid = [[None for _ in range(n)] for _ in range(n)]
    assert len(grid) == n
    assert len(grid[0]) == n
    if n == 1:
        return [[1]]
    if n == 0:
        return [[]]

    print(f"left to right")
    while True:
        if set(r, c, x, grid):
            x += 1
            c += 1
        else:
            break
    c -= 1
    r += 1
    show(grid, r, c, x)

    print(f"top down")
    while True:
        if set(r, c, x, grid):
            x += 1
            r += 1
        else:
            break
    r -= 1
    c -= 1
    show(grid, r, c, x)

    print(f"right to left")
    while True:
        if set(r, c, x, grid):
            x += 1
            c -= 1
        else:
            break
    c += 1
    r -= 1
    show(grid, r, c, x)

    print(f"bottom up")
    while True:
        if set(r, c, x, grid):
            x += 1
            r -= 1
        
        else:
            break
    r += 1
    c += 1
    show(grid, r, c, x)

    if grid[r][c] is None:
        return solve(n, r, c, x, grid)
    else:
        return grid




@pytest.mark.parametrize('n, expected', [
    (3, [
            [ 1, 2, 3 ],
            [ 8, 9, 4 ],
            [ 7, 6, 5 ]
        ]),
    (4, [
            [ 1, 2, 3, 4],
            [12,13,14, 5],
            [11,16,15, 6],
            [10, 9, 8, 7]
        ]),
    (5, [
            [ 1, 2, 3, 4, 5],
            [16,17,18,19, 6],
            [15,24,25,20, 7],
            [14,23,22,21, 8],
            [13,12,11,10, 9]
        ])
]) # yapf: disable
def test(n, expected):
    out = solve(n)
    assert out == expected