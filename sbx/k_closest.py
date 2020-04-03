import math
from operator import itemgetter
from typing import *

import pytest


def k_closest(points: List[List[int]], K: int) -> List[List[int]]:
    distances = [{
        'pos': (x, y),
        'dis': math.sqrt(x**2 + y**2)
    } for x, y in points]
    print(f"distances={distances}")
    s = sorted(distances, key=itemgetter('dis'))[0:K]
    print(f"sorted={s}")
    out = [[d['pos'][0], d['pos'][1]] for d in s]

    return out


@pytest.mark.parametrize('arg, k, expected', [
    ([[1,3],[-2,2]], 1, [[-2,2]]),
])  # yapf: disable
def test(arg, k, expected):
    assert k_closest(arg, k) == expected