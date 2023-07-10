
def edge_list():
    n = int(input('Введите n'))
    m = int(input('Введите m'))
    edges = [(0, 0) for _ in range(m)]
    for i in range(m):
        a = int(input('Введите a'))
        b = int(input('Введите b'))
        edges[i] = (a, b)
    print(edges)


def contiguity_matrix():
    n = int(input('Введите n'))
    m = int(input('Введите m'))
    matrix = [[int(0) for _ in range(n)] for _ in range(n)]
    for i in range(m):
        a = int(input('Введите a'))
        b = int(input('Введите b'))
        a -= 1
        b -= 1
        matrix[a][b] = 1
        matrix[b][a] = 1
    print(matrix)


def contiguity_list():
    n = int(input())
    m = int(input())
    matrix = [[] for _ in range(n)]
    for i in range(m):
        a = int(input())
        b = int(input())
        a -= 1
        b -= 1
        matrix[a].append(b)
        matrix[b].append(a)
    print(matrix)


contiguity_list()