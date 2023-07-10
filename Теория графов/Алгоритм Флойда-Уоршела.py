"""
Отличается от алгоритма Дейкстры тем, что в первом мы от одной вершины
находим расстояние до всех остальных, а в этом мы находим расстояние от всех
вершин до всех остальных.
Идея алгоритма в том, чтобы разбить пути на фазы.
Сложность O(n^3)
"""

def dijkstra(graph, start_vertex):
    inf = 1000000
    dist = [inf for _ in range(len(graph))]
    dist[start_vertex] = 0
    s = []
    s.append([0, start_vertex])

    while len(s) != 0:
        current_vertex = s[0][-1]
        s.pop(0)
        for i in range(len(graph[current_vertex])):
            adjacent_vertex = graph[current_vertex][i][0]
            weight = graph[current_vertex][i][-1]
            if dist[current_vertex] + weight < dist[adjacent_vertex]:
                try:
                    s.remove([dist[adjacent_vertex], adjacent_vertex])
                except ValueError:
                    pass
                dist[adjacent_vertex] = dist[current_vertex] + weight
                s.append([dist[adjacent_vertex], adjacent_vertex])
    return dist


def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist



def test():
    graph = [
        [[1, 10], [5, 5]],
        [[0, 10], [2, 1]],
        [[1, 1], [3, 5], [5, 7], [6, 10]],
        [[2, 5], [4, 1]],
        [[3, 1], [6, 2]],
        [[0, 5], [2, 7], [6, 100], [7, 3]],
        [[2, 10], [4, 2], [5, 100], [7, 8], [8, 100]],
        [[5, 3], [6, 8], [9, 1]],
        [[6, 100], [9, 1]],
        [[7, 1], [8, 1]]
    ]

    inf = 1000000
    graph2 = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph2[i][graph[i][j][0]] = graph[i][j][-1]
            graph2[graph[i][j][0]][i] = graph[i][j][-1]

    for i in range(0, len(graph)):
        dist = dijkstra(graph, i)
        print(dist)
    print(end='\n')
    dist = floyd_warshall(graph2)
    for i in range(0, len(dist)):
        print(dist[i])



test()