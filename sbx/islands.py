from __future__ import annotations

import json
from copy import copy
from typing import *

import pytest
from dotenv import load_dotenv

load_dotenv('.env')


class Solution:
    """https://leetcode.com/problems/number-of-islands/"""
    def dfs(self, grid: List[List[str]], ri: int, ci: int):
        grid[ri][ci] = '0'
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r = ri + dr
            c = ci + dc
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue
            elif grid[r][c] == '1':
                self.dfs(grid, r, c)

    def numIslandsDfs(self, grid: List[List[str]]) -> int:
        rc = len(grid)
        if not rc:
            return 0
        cc = len(grid[0])
        islands = 0
        for ri in range(rc):
            for ci in range(cc):
                if grid[ri][ci] == '1':
                    islands += 1
                    self.dfs(grid, ri, ci)
        return islands

    def bfs(self, grid: List[List[str]], ri: int, ci: int):
        grid[ri][ci] = '0'
        next_steps = []
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r = ri + dr
            c = ci + dc
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue
            elif grid[r][c] == '1':
                next_steps.append([r, c])
        for r, c in next_steps:
            self.bfs(grid, r, c)

    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        rc = len(grid)
        if not rc:
            return 0
        cc = len(grid[0])
        islands = 0
        for ri in range(rc):
            for ci in range(cc):
                if grid[ri][ci] == '1':
                    islands += 1
                    self.bfs(grid, ri, ci)
        return islands


@pytest.mark.parametrize('digits, expected', [
    ([["0"]], 0),
    ([["0", "0", "0"]], 0),
    ([["1", "1", "1"]], 1),
    ([["1", "0", "1"]], 2),
    ([["1", "0", "1"],
      ["1", "0", "1"],
      ["1", "1", "1"],
      ["0", "0", "0"]], 1),
    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]], 1),
    ([["1","0","1","1","1"],
      ["1","0","1","0","1"],
      ["1","1","1","0","1"]], 1)
]) # yapf: disable
def test(digits, expected):
    s = Solution()
    output = s.numIslandsBfs(digits)
    assert output == expected
