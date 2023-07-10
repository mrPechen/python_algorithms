from queue import Queue

# Сложность(n*(n+m))
def bfs(graph, start_vertex):
    used = [int(-1) for _ in range(len(graph))]
    used[start_vertex] = 0
    q = Queue()
    q.put(start_vertex)
    while not q.empty():
        current_vertex = q.get()
        for i in range(len(graph[current_vertex])):
            adjacent_vertex = graph[current_vertex][i]
            if used[adjacent_vertex] == -1:
                q.put(adjacent_vertex)
                used[adjacent_vertex] = used[current_vertex] + 1
    print(used)
    for i in range(len(used)):
        print(f'{i+1} = {used[i]}')


def test():
    graph = [
        [1, 2],
        [0, 3, 6],
        [0, 3],
        [1, 2, 4, 5, 6],
        [3, 7],
        [3, 7],
        [1, 3, 7],
        [4, 5, 6, 8],
        [7]
    ]

    bfs(graph, 0)


test()
