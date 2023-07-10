"""
Алгоритмы помогают найти во взвешенном грефе поддерево этого графа, которое
соединяло бы все его вершины и при этом сумма всех ребер была минимальна из всех
возможных.

Существуют 2 алгоритма для этих целей:

1. Алгоритм Крускала. (будет в коде)
Стандартный - Сложность O(m*log(n)+n^2)
С системой непересекающихся множеств - сложность O(m*log(n))

2. Алгоритм Прима

"""


parent = [i for i in range(7)]
sizes = [int(1) for _ in range(7)]


def find_set(v):
    if v == parent[v]:
        return v
    return find_set(parent[v])


def union_set(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if sizes[a] < sizes[b]:
            a, b = b, a
        parent[b] = a
        sizes[a] += sizes[b]


def test():

    edges = [
        [1, 2, 5],
        [1, 3, 9],
        [1, 5, 1],
        [1, 6, 3],
        [2, 4, 8],
        [2, 6, 3],
        [3, 5, 4],
        [4, 6, 7],
        [5, 6, 2],
    ]
    edges = sorted(edges, key=lambda x: x[2])
    all_cost = 0
    for i in range(len(edges)):
        a = edges[i][0]
        b = edges[i][1]
        c = edges[i][2]

        if find_set(a) != find_set(b):
            print(a, b)
            all_cost += c
            union_set(a, b)
    print(all_cost)

test()