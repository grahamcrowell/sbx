from __future__ import annotations

from typing import Any


class ListNode:
    data: Any
    nn: ListNode

    def __init__(self, data: Any):
        self.data = data
        self.nn = None

    def to_list(self) -> List[Any]:
        if self.data == None:
            return []

        current = self
        out = []
        while current.nn != None:
            out.append(current.data)
            current = current.nn
        out.append(current.data)
        return out

    @staticmethod
    def from_list(l: List[Any]) -> ListNode:
        if len(l) == 0:
            return ListNode(None)
        else:
            head = current = ListNode(l[0])
            for x in l[1:]:
                current.nn = ListNode(x)
                current = current.nn
            return head


def test_foo():
    x = list(range(10))
    y = ListNode.from_list(x)
    assert x == y.to_list()

@pytest.mark.parametrize("l", [
        (list(range(10))),
        ([]),
        ([1])
    ]
) # yapf: disable
def test_main(l):
    ll: ListNode = ListNode.from_list(l)
    assert l == ll.to_list()
