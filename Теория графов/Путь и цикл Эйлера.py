
"""
Эйлеров путь - это путь в графе, который проходит по всем ребрам только
1 раз.

Эйлеров цикл - это тот же Эйлеров путь, но только начинающийся и заканчивающийся
в одной и той же вершине. Он существует только в том случае, если степени всех наших
вершин четные числа.
Сложность O(m), где m это кол-во ребер в нашем графе.
"""


def dfs(graph, edges, cycle, current_vertex):

    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        a = current_vertex
        b = adjacent_vertex
        if a > b:
            a, b = b, a

        if edges[(a, b)] != 0:
            #edges.pop((a, b))
            edges[(a, b)] = 0
            dfs(graph, edges, cycle, adjacent_vertex)

    cycle.append(current_vertex)


def test():
    graph = [
        [1, 3, 4],
        [0, 2, 3, 4],
        [1, 3],
        [0, 1, 2, 4],
        [0, 1, 3]
    ]

    odd_vertices = []
    # для вершин с четной степенью
    for i in range(len(graph)):
        if len(graph[i]) % 2 == 1:
            odd_vertices.append(i)
    if len(odd_vertices) > 2:
        print('нет цикла и пути')
        return False
    elif len(odd_vertices) == 2:
        graph[odd_vertices[0]].append(odd_vertices[1])
        graph[odd_vertices[1]].append(odd_vertices[0])

    cycle = [0]
    edges = {}

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if i < graph[i][j]:
                edges[(i, graph[i][j])] = i+1

    dfs(graph, edges, cycle, 0)
    for i in range(len(cycle)):
        print(cycle[i] + 1)
    print(cycle)

    # для вершин без четной степени
    if len(odd_vertices) == 2:
        for i in range(1, len(cycle)-2):
            if cycle[i-1] == odd_vertices[0] and cycle[i] == odd_vertices[1] or cycle[i-1] == odd_vertices[1] and cycle[i] == odd_vertices[0]:
                new_cycle = []
                for j in range(i, i+len(cycle)):
                    index = j % len(cycle)
                    if index == 0:
                        continue
                    new_cycle.append(cycle[index])
                cycle = new_cycle

    for i in range(len(cycle)):
        print(cycle[i]+1)
    print(cycle)


test()