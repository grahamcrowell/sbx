from typing import *


def merge_sort(arr: List[int]) -> List[int]:
    """
    paradigm: Divide and Conquer
    stable:   YES
    average:  O = n*log(n)
    worst:    O = n*log(n)
    best:     O = n*log(n)
    notes:    works well on linked lists
    refs:     https://www.geeksforgeeks.org/merge-sort/
    """
    if len(arr) <= 1:
        return arr
    # divide
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    assert len(L) <= len(R)

    # resursive
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


import pytest


@pytest.mark.parametrize('arr, expected', [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
])
def test(arr, expected):
    assert merge_sort(arr) == expected