from __future__ import annotations

import json
from copy import copy
from queue import Queue
from typing import *

import pytest
from dotenv import load_dotenv
from rope.base.oi.type_hinting.utils import parametrize_type

load_dotenv('.env')


class Solution:
    def build_path(self, matrix: List[List[int]], row, col):
        path = []
        r, c = row, col
        n, m = len(matrix), len(matrix[0])

        if row == 0 or col == m - 1:
            print(f"down (+row) and left (-col)")
            while r >= 0 and r < n and c >= 0 and c < m:
                path.append((r, c))
                r += 1
                c -= 1

        elif col == 0 or row == n - 1:
            print(f"up (-row) and right (+col)")
            while r >= 0 and r < n and c >= 0 and c < m:
                path.append((r, c))
                r -= 1
                c += 1

        else:
            raise Exception('cant happen')
        return path

    def build_parameter(self, matrix: List[List[int]]) -> List[Tuple[int]]:
        perimeter = [(0, 0)]
        n, m = len(matrix), len(matrix[0])

        # build top right
        top_right = []
        ri = 0
        for ci in range(1, m):
            top_right.append((ri, ci))
        ci = m - 1
        for ri in range(1, n):
            top_right.append((ri, ci))
        self.top_right = top_right

        # build left bottom
        ci = 0
        left_bottom = []
        for ri in range(1, n):
            left_bottom.append((ri, ci))
        for ci in range(1, m):
            left_bottom.append((ri, ci))
        self.left_bottom = left_bottom
        perimeter.extend(self.top_right)
        perimeter.extend(self.left_bottom)
        assert (n - 1, m - 1) == perimeter[-1], ((n - 1, m - 1), perimeter)
        assert len(perimeter) == n * 2 + m * 2 - 3
        return perimeter

    def get_next_start(self, matrix: List[List[int]], r1, c1) -> Tuple[int]:
        perimeter = self.build_parameter(matrix)
        next_start_index = perimeter[perimeter.index((r1, c1)) + 1]
        print(f"perimeter.index((r1, c1))={perimeter.index((r1, c1))}")
        print(
            f"perimeter[perimeter.index((r1, c1))]={perimeter[perimeter.index((r1, c1))]}"
        )
        print(f"next_start_index={next_start_index}")
        return next_start_index

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        r0, c0 = 0, 0
        self.build_parameter(matrix)

        path = [(r0, c0)]
        values = [matrix[r0][c0]]

        n, m = len(matrix), len(matrix[0])
        if n < 2 or m < 2:
            raise NotImplementedError('fixme')

        r0, c0 = 0, 1
        safety = 10
        while True and safety > 0:
            safety -= 1
            diag_path = self.build_path(matrix, r0, c0)
            print(f'diag_path={diag_path}')
            path.extend(diag_path)
            print(f'path={path}')
            diag_order = list(
                map(lambda ri_ci: matrix[ri_ci[0]][ri_ci[1]], path))
            print(f"diag_order={diag_order}")
            
            r1, c1 = path[-1]
            if (r1, c1) in self.left_bottom:
                next_index = self.left_bottom.index((r1, c1)) + 1 
                if next_index < len(self.left_bottom):
                    r0, c0 = self.left_bottom[next_index]
            else:
                next_index = self.top_right.index((r1, c1)) + 1 
                if next_index < len(self.top_right):
                    r0, c0 = self.top_right[next_index]
            print(f'next_start={(r0, c0)}')
            if r0 == n - 1 and c0 == m - 1:
                path.append((n - 1, m - 1))
                print(f"path = {path}")
                return list(map(lambda r_c: matrix[r_c[0]][r_c[1]], path))


def test_perimeter():
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]] # yapf: disable
    r_d = [(0,1),(0,2),(1,2),(2,2)] # yapf: disable
    d_r = [(1,0),(2,0),(2,1),(2,2)] # yapf: disable
    s = Solution()
    p = [(0, 0)]
    p.extend(r_d)
    p.extend(d_r)
    assert p == s.build_parameter(m)


def test_next_start():
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]] # yapf: disable
    s = Solution()
    assert (1, 2) == s.get_next_start(m, 0, 2)


@pytest.mark.parametrize('matrix, expected',[
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
      [1, 2, 4, 7, 5, 3, 6, 8, 9])
    ]) # yapf: disable
def test(matrix, expected):
    s = Solution()
    assert expected == s.findDiagonalOrder(matrix)