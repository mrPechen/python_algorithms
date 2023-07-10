"""
Это структура данных, которая предоставляет возможности:
1. Union set(x, y) Сложность O() - Объединить множества, в которых находятся элементы x и y.

2. Find set(x) (Сложность O(log(n)) - Узнать в каком из множеств находится конкретный элемент.

3. Make set(x) Сложность O(1) - Создать новый элемент и поместить его в конкретное множество

Общая сложность O(1)
"""

parent = [i for i in range(10)]
sizes = [int(1) for _ in range(10)]
print(parent)


def find_set(v):
    if v == parent[v]:
        return v
    print(parent)
    parent[v] = find_set(parent[v])
    print(parent)
    return parent[v]


def union_set(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if sizes[a] < sizes[b]:
            a, b = b, a
        parent[b] = a
        sizes[a] += sizes[b]
    print(sizes)


def test():
    print(find_set(0))
    print(find_set(1))

    union_set(0, 1)

    print(find_set(0))
    print(find_set(1))

    union_set(1, 2)
    union_set(2, 3)
    union_set(3, 4)
    union_set(4, 5)

    print(find_set(0))
    print(find_set(1))
    print(find_set(2))
    print(find_set(3))
    print(find_set(4))
    print(find_set(5))
    print(find_set(6))




test()
