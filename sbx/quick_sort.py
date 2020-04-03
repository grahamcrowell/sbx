from typing import *

import pytest


def quick_sort(arr: List[int], lo=None, hi=None) -> List[int]:
    """
    paradigm: Divide and Conquer
    stable:   NO, by default but can be made so by considering indexes
    average:  O = n*log(n)
    worst:    O = n**2
    best:     O = n*log(n)
    in place: YES
    notes:    several versions differ by partitioning scheme
    refs:     https://www.geeksforgeeks.org/quick-sort/
    """
    # trivial case
    if len(arr) < 2:
        return arr
    # handle initial call
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(arr) - 1
    # start of algorithm
    if lo < hi:

        pi = partition(arr, lo, hi)

        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)


def partition(arr: List[int], lo: int, hi: int):
    # choose last value as pivot
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            # swap i and j
            arr[i], arr[j] = arr[j], arr[i]

    # swap i + 1 and hi
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


@pytest.mark.parametrize('arr, expected', [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
    ([3, 1, 2, 3, 1, 2],[1, 1, 2, 2, 3, 3])
]) # yapf: disable
def test(arr, expected):
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == expected