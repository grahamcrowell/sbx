def rotate(s: str) -> Set[str]:
    out = set()
    curr = s
    out.add(curr)
    # print(curr)
    # print(out)
    for _ in range(len(s) - 1):
        curr = str(curr[1:]) + str(curr[0])
        # print(curr)
        if curr == s:
            break
        # print(curr)
        out.add(curr)
    return out


def swap(s: str, i: int, j: int):
    assert i < j
    stuff = s[i + 1:j]
    pre = s[0:i]
    sw = s[j] + stuff + s[i]
    post = s[j + 1:]
    return pre + sw + post




def perm(s: str) -> Set[str]:
    out = set()
    for i in range(len(s) - 1):
        curr = s
        print(f"i = {i}")
        for j in range(i + 1, len(curr)):
            print(f"j = {j}")
            curr = swap(curr, i, j)
            temp: Set[str] = rotate(curr)
            out = out.union(temp)
            assert len(s) == len(curr), i
    print(f"out={out}")
    return out


def test_swap():
    idx = 0
    s = 'abc'
    assert 'bac' == swap(s, idx, idx + 1)


def test_rotate():
    assert rotate('abc') == set(['abc', 'bca', 'cab'])

