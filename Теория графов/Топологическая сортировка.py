"""
Для этого алгоритма граф должен быть без циклов.
Суть этой сортировки в том, чтобы перенумеровать все вершины графа так,
чтобы каждое ребро вело из вершины с меньшим номером в вершину с большим.

"""


def dfs(graph, used, order, current_vertex):
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs(graph, used, order, adjacent_vertex)
    order.append(current_vertex)


def test():
    graph = [
        [4],
        [0],
        [3, 1],
        [0, 1, 4],
        []
    ]

    used = [int(0) for _ in range(len(graph))]
    order = []
    for i in range(len(graph)):
        if used[i] == 0:
            dfs(graph, used, order, i)
    order.reverse()
    for i in range(len(graph)):
        print(f'Переименовать вершину {i+1} -> в {order[i]+1}')

test()