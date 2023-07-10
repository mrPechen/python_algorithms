# Сложность O(n+m)

def dfs_list(graph, used, current_vertex):
    print(current_vertex+1, end=' ')
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_list(graph, used, adjacent_vertex)



def test():
    graph = [
        [4, 5],
        [3],
        [3],
        [1, 2, 9],
        [0],
        [0],
        [],
        [8],
        [7],
        [3]
    ]

    used = [int(0) for _ in range(len(graph))]
    for i in range(len(graph)):
        if not used[i]:
            print(dfs_list(graph, used, i))




test()