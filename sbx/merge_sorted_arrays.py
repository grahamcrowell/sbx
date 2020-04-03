from __future__ import annotations

import json
from copy import copy
from typing import *

import pytest
from dotenv import load_dotenv

load_dotenv('.env')


class Solution:
    def merge_step(self, idx: int, nums1: List[int], m: int, idx1: int,
                   nums2: List[int], n: int, idx2: int):
        if idx1 < 0:
            print('idx1 < 0')
            nums1[idx] = nums2[idx2]
            nums2[idx2] = None
            idx2 -= 1
            idx -= 1
        elif idx2 < 0:
            print('idx2 < 0')
            nums1[idx] = nums1[idx1]
            nums1[idx1] = None
            idx1 -= 1
            idx -= 1
        elif nums1[idx1] >= nums2[idx2]:
            print('num1 >= num1')
            nums1[idx] = nums1[idx1]
            nums1[idx1] = None
            idx1 -= 1
            idx -= 1
        else:
            print('num1 < num2')
            nums1[idx] = nums2[idx2]
            nums2[idx2] = None
            idx2 -= 1
            idx -= 1
        return idx, idx1, idx2

    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for idx, n2 in enumerate(nums2):
                nums1[idx] = n2
            return
        if n == 0:
            return

        idx1 = m - 1
        idx2 = n - 1
        idx = n + m - 1

        while nums2[0] is not None:
            if idx1 < 0:
                print('idx1 < 0')
                nums1[idx] = nums2[idx2]
                nums2[idx2] = None
                idx2 -= 1
                idx -= 1
            elif idx2 < 0:
                print('idx2 < 0')
                nums1[idx] = nums1[idx1]
                nums1[idx1] = None
                idx1 -= 1
                idx -= 1
            elif nums1[idx1] >= nums2[idx2]:
                print('num1 >= num1')
                nums1[idx] = nums1[idx1]
                nums1[idx1] = None
                idx1 -= 1
                idx -= 1
            else:
                print('num1 < num2')
                nums1[idx] = nums2[idx2]
                nums2[idx2] = None
                idx2 -= 1
                idx -= 1

            print(f"nums1={nums1}")
            print(f"nums2={nums2}")
            print(
                f"idx={idx}, idx1={idx1} ({nums1[idx1]}), idx2={idx2} ({nums2[idx2]})"
            )




@pytest.mark.parametrize('nums1,nums2,expected', [
                         ([1, 2, 3, 0, 0, 0], [2, 5, 6],
                         [1, 2, 2, 3, 5, 6]),
                         ([1, 2, 3, 0, 0, 0, 0], [1, 2, 5, 6],
                         [1, 1, 2, 2, 3, 5, 6]),
                         ([0, 0, 0, 0], [1, 2, 5, 6],
                         [1, 2, 5, 6]),
                         ([1, 2, 5, 6], [],
                         [1, 2, 5, 6])
                        ]) # yapf: disable
def test_merge_array(nums1, nums2, expected):
    l1 = copy(nums1)
    l2 = copy(nums2)
    n = len(l2)
    m = len(l1) - n
    s = Solution()
    s.merge(l1, m, l2, n)
    assert expected == l1
