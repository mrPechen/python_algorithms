"""
Дерево отрезков - это структура данных, которая позволяет эффективно
реализовывать операции следующего вида:

1. Нахождение минимума суммы элементов массива от L до R, где L и R могут быть
любыми числами. Сложность O(log(n))
2. Изменение элементов массива. Как одного элемента, так и целого отрезка
от L до R. Сложность O(log(n))

Память при использовании дерева отрезков = O(n).
"""
n = 8 # длина массива а
tree = [int(0) for _ in range(4*n)]


def build_tree(a, v=1, l=0, r=n-1):
    if l == r:
        tree[v] = a[l]
        return
    m = int((l + r) / 2)
    build_tree(a, v*2, l, m)
    build_tree(a, v * 2+1, m+1, r)
    tree[v] = tree[2*v] + tree[2*v+1]


def get_sum(i, j, v=1, l=0, r=n-1):
    if i == l and j == r:
        return tree[v]
    m = int((l + r) / 2)
    if m >= j:
        return get_sum(i, j, v*2, l, m)
    elif m < i:
        return get_sum(i, j, v*2+1, m+1, r)
    else:
        return get_sum(i, m, v*2, l, m) + get_sum(m+1, j, v*2+1, m+1, r)


def update(i, x, v=1, l=0, r=n-1):
    if l == r:
        tree[v] = x
        return
    m = int((l + r) / 2)
    if i <= m:
        update(i, x, v*2, l, m)
    else:
        update(i, x, v*2+1, m+1, r)
    tree[v] = tree[2 * v] + tree[2 * v + 1]


def test():
    a = [1, 2, 3, 4, 5, 6, 7, 8]

    build_tree(a)
    print(get_sum(1, 6))
    update(3, 10)
    print(get_sum(1, 6))


test()