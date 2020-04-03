"""https://leetcode.com/problems/maximum-subarray/
"""

from typing import *


class Solution:
    def max_sub_array(self, arr: List[int]) -> List[int]:
        curr = []
        max_elem = max(arr)
        max_idx = arr.index(max_elem)
        
        for i, x in enumerate(arr):
            if not curr and x > 0:
                curr.append(x)
            elif x > 0:
                cur_sum = sum(curr)


        pos_idx = [i for i in range(len(arr)) if arr[i] > 0]
        a, b = min(pos_idx), max(pos_idx)


            


def test():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sub = [4, -1, 2, 1]
    output = Solution().max_sub_array(arr)
    assert output == max_sub