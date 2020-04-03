# @pytest.mark.parametrize('n, connections, expected', [
#     # (4, [[0,1],[1,2],[2,0],[3,4]], [[1,3]]),
#     # (4, [[0,1],[1,2],[2,0],[1,3]], [[1,3]]),
#     (6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]], [[1,3]])
# ]) # yapf: disable
# def test(n, connections, expected):
#     assert False
#     out = solve(n, connections)
#     assert out == expected
from copy import copy, deepcopy
from itertools import chain, groupby, permutations
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


def get_component_with(edges, node, visited=None):
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
        visited = visited.union(get_component_with(edges, new_node, visited))
    return visited


class Graph:
    def __init__(self, edges, nodes=None):
        self._edges = set(normalize(edges))
        if nodes:
            self._nodes = set(chain(*edges)).union(nodes)
        else:
            self._nodes = set(chain(*edges))
        self._adj = None
        self._degree = None

    @property
    def adj(self) -> Dict[int, List[int]]:
        if self._adj is None:
            adj = DefaultDict(list)
            for edge in self._edges:
                adj[edge[0]].append(edge[1])
                adj[edge[1]].append(edge[0])
            self._adj = adj
        return self._adj

    @property
    def degree(self) -> Dict[int, int]:
        if self._degree is None:
            self._degree = {key: len(elems) for key, elems in self.adj.items()}
        return self._degree

    def _get_component(self, node) -> Set[int]:
        return get_component_with(self._edges, node)

    def get_components(self) -> List[Set[int]]:
        components = sorted(self._disconnected_nodes())
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

    def _disconnected_nodes(self):
        return self._nodes.difference(set(chain(*self._edges)))

    def remove_edge(self, edge):
        assert edge in self._edges
        edges = deepcopy(self._edges)
        nodes = deepcopy(self._nodes)
        edges.remove(edge)
        return Graph(edges, nodes)

    def get_critical_edges(self):
        # FIXME
        # all nodes with degree 1 are in a critical connection
        critical_connections = set()
        for key, degree in self.degree.items():
            if degree == 1:
                critical_connections.add(edges_with(self._edges, key).pop())
        # iterate over each edge, remove it then count components
        edges = deepcopy(self._edges).difference(critical_connections)
        for edge in edges:
            print(f"\n\nedge={edge}")
            sub_graph = self.remove_edge(edge)
            components = sub_graph.get_components()
            print(f"components={components}")
            if len(components) > 1:
                print(f"critical connection: {edge}")
                critical_connections.add(edge)
        return critical_connections


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
    component = get_component_with(edges, node)
    assert component == set(normalize(edges))


def test_get_components():
    expected = [{(0, 1), (1, 2), (1, 3), (4, 5), (3, 4), (0, 2), (3, 5)},
                {(10, 11)}, {(10, 12)}]
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3], [10, 11],
             [10, 12]]
    node = 0
    g = Graph(edges)
    components = g.get_components()
    print(f"components={components}")
    assert components == expected

    edges = {(0, 1), (1, 2), (2, 3), (4, 5), (0, 5), (0, 666)}


def test_critical_connections():
    cycle = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)]
    critical = (0, 666)
    edges = [*cycle, critical]
    g = Graph(edges)
    assert len(g.get_critical_edges()) == 1