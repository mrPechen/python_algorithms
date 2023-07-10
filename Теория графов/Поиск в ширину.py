from queue import Queue
"""
BFS проходит по первой вершине и ее соседям, потом по соседям соседних вершин и тд.
Сложность O(n+m) при хранении в списке смежностей
Сложность O(n^2) при хранении в матрице смежностей
BFS и DFS основные алгоритмы в теории графов.
"""


def bfs_list(graph):
    start_vertex = 0
    used = [int(0) for _ in range(len(graph))]
    used[start_vertex] = 1
    q = Queue()
    q.put(start_vertex)

    while not q.empty():
        current_vertex = q.get()
        print(current_vertex+1)
        for i in range(len(graph[current_vertex])):
            adjacent_vertex = graph[current_vertex][i]
            if not used[adjacent_vertex]:
                q.put(adjacent_vertex)
                used[adjacent_vertex] = 1


def bfs_matrix(graph):
    start_vertex = 0
    used = [int(0) for _ in range(len(graph))]
    used[start_vertex] = 1
    q = Queue()
    q.put(start_vertex)

    while not q.empty():
        current_vertex = q.get()
        print(current_vertex+1)

        for i in range(len(graph[current_vertex])):
            if graph[current_vertex][i] == 1:
                adjacent_vertex = i
                if not used[adjacent_vertex]:
                    q.put(adjacent_vertex)
                    used[adjacent_vertex] = 1


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

    bfs_list(lst)

    bfs_matrix(matrix)

test()