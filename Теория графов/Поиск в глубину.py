"""Идея DFS заключается в том, что из каждой вершины мы идем в вершину
в которой еще не были
Сложность O(n+m) если для хранения используется список
Сложность O(n^2) если используется матрица смежностей"""


def dfs_list(graph, used, current_vertex):
    print(current_vertex+1)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_list(graph, used, adjacent_vertex)


def dfs_matrix(graph, used, current_vertex):
    print(current_vertex+1)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        if graph[current_vertex][i] == 1:
            if used[i] != 1:
                dfs_matrix(graph, used, i)


def test():
    lst = [
        [1, 3],
        [0, 5, 6],
        [6],
        [0, 4],
        [3, 7],
        [1, 6],
        [1, 2, 5],
        [4]
    ]

    matrix = [
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0]
    ]

    n = 8
    used = [int(0) for _ in range(n)]
    dfs_list(lst, used, 0)

    used.clear()
    used = [int(0) for _ in range(n)]
    dfs_matrix(matrix, used, 0)

test()