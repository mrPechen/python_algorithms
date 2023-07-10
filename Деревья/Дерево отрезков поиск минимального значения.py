n = 8 # длина массива а
tree = [int(0) for _ in range(4*n)]


def build_tree(a, v=1, l=0, r=n-1):
    if l == r:
        tree[v] = a[l]
        return
    m = int((l + r) / 2)
    build_tree(a, v*2, l, m)
    build_tree(a, v * 2+1, m+1, r)
    tree[v] = min(tree[2*v], tree[2*v+1])


def min_query(i, j, v=1, l=0, r=n-1):
    if i == l and j == r:
        return tree[v]
    m = int((l + r) / 2)
    if m >= j:
        return min_query(i, j, v*2, l, m)
    elif m < i:
        return min_query(i, j, v*2+1, m+1, r)
    else:
        return min(min_query(i, m, v*2, l, m), min_query(m+1, j, v*2+1, m+1, r))


def update(i, x, v=1, l=0, r=n-1):
    if l == r:
        tree[v] = x
        return
    m = int((l + r) / 2)
    if i <= m:
        update(i, x, v*2, l, m)
    else:
        update(i, x, v*2+1, m+1, r)
    tree[v] = min(tree[2*v], tree[2*v+1])


def test():
    a = [1, 2, 3, 4, 5, 6, 7, 8]

    build_tree(a)
    print(min_query(1, 6))
    update(3, 10)
    print(min_query(1, 6))
    update(1, 20)
    print(min_query(1, 6))



test()