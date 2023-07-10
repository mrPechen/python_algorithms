# сложность O(n*k*m), память O(n*k)

def matrix_mul(a, b):
    n = len(a)
    m = len(a[0])
    kk = len(b[0])
    c = [[i for i in range(n)] for j in range(kk)]
    for i in range(n):
        for j in range(kk):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]

    print(c)

    return c


def test():
    a = [
        [1, 2, 3],
        [3, 1, 2]
    ]
    b = [
        [1, 2],
        [3, 2],
        [1, 2]
    ]
    c = [
        [10, 12],
        [8, 12]
    ]
    print(matrix_mul(a, b) == c)
test()