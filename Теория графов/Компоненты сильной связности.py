"""
Компоненты сильной связности - это набор вершин в графе, где
если мы начнем из любой вершины этого множества, то сможем попасть в
любую вершину в этом же множестве.

"""


def dfs(graph, used, order, current_vertex):
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs(graph, used, order, adjacent_vertex)
    order.append(current_vertex)


def dfs_reverse(graph, used, component, current_vertex):
    component.append(current_vertex)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_reverse(graph, used, component, adjacent_vertex)


def test():
    graph = [
        [2],
        [0, 2],
        [3, 4],
        [],
        [1, 8],
        [10],
        [5],
        [1, 5],
        [9],
        [8],
        [6, 7]
    ]

    used = [int(0) for _ in range(len(graph))]
    order = []
    for i in range(len(graph)):
        if not used[i]:
            dfs(graph, used, order, i)
    print(order)
    order.reverse()
    print(order)

    revers_graph = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            revers_graph[graph[i][j]].append(i)
    used = [int(0) for _ in range(len(graph))]
    for i in range(len(order)):
        if not used[order[i]]:
            component = []
            dfs_reverse(revers_graph, used, component, order[i])

            for e in component:
                print(e+1)
    print(revers_graph)


test()

