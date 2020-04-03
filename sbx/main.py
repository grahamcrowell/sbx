from itertools import chain, permutations
from math import factorial
from typing import *

import pytest
from docutils.transforms import components


def normalize(edges):
    return list(
        map(lambda edge: (min(edge[0], edge[1]), max(edge[0], edge[1])),
            edges))


def edges_with(edges, node) -> Set[int]:
    edges = normalize(edges)
    # print(f'edges_with={edges, node}')
    tmp = list(chain(*edges))
    out = set()
    start = 0
    while start < len(edges):
        try:
            idx = tmp.index(node, start)
        except ValueError:
            # print("ValueError")
            return set(out)
        else:
            edge = edges[idx // 2]
            out.add(edge)
            start = idx + 2
    return out


def neighbors(edges, node):
    return set(chain(*edges_with(edges, node))) - set([node])


class Visitor:
    def __init__(self):
        self.visited = list()

    def visit(self, node):
        self.visited.append(node)


def dfs(edges, node, visited=None):
    if visited is None:
        visited = set()
        edges = set(normalize(edges))
    else:
        pass
        # print(f"visited={visited}")
    remaining_edges = edges - visited
    # print(f"remaining_edges={remaining_edges}")
    connected_edges = edges_with(remaining_edges, node)
    # print(f"connected_edges={connected_edges}")
    for visited_edge in connected_edges:
        visited.add(visited_edge)
        if visited_edge[0] == node:
            new_node = visited_edge[1]
        else:
            new_node = visited_edge[0]
        visited = visited.union(dfs(edges, new_node, visited))
    return visited


class Solver:
    def __init__(self, edges):
        self._edges = set(normalize(edges))
        self._nodes = set(chain(*edges))

    def _get_component(self, node) -> Set[int]:
        return dfs(self._edges, node)

    def get_components(self) -> List[Set[int]]:
        components = []
        edges = self._edges
        print(f"edges={edges}")
        while edges:
            init_edge = edges.pop()
            edges.add(init_edge)
            node = init_edge[0]
            component = self._get_component(node)
            components.append(component)
            visited = set(chain(component))
            print(f"visited={visited}")
            edges -= visited
            print(f"edges={edges}")
        return components



def solve(edges):
    pass


def test_edges_with():
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    node = 0
    assert edges_with(edges, node) == set([(0, 1), (0, 2)])


def test_neighbors():
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    node = 0
    assert neighbors(edges, node) == {1, 2}


def test_dfs():
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    node = 0
    component = dfs(edges, node)
    assert component == set(normalize(edges))


def test_get_components():
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3], [10,11], [10,12]]
    node = 0
    s = Solver(edges)
    components = s.get_components()
    print(f"components={components}")

    assert False
    
# @pytest.mark.parametrize('n, connections, expected', [
#     # (4, [[0,1],[1,2],[2,0],[3,4]], [[1,3]]),
#     # (4, [[0,1],[1,2],[2,0],[1,3]], [[1,3]]),
#     (6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]], [[1,3]])
# ]) # yapf: disable
# def test(n, connections, expected):
#     assert False
#     out = solve(n, connections)
#     assert out == expected