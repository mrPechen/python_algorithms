def bin_pow(a, n, mod):
    res = [[_ for _ in range(len(a))] for _ in range(len(a))]
    for i in range(len(res)):
        res[i][i] = 1
    while n != 0:
        if n & 1:
            res = matrix_mul(res, a, mod)
        n >>= 1
        a = matrix_mul(a, a, mod)
    return res


def matrix_mul(a, b, mod):
    n = len(a)
    m = len(a[0])
    kk = len(b[0])

    c = [[int(0) for _ in range(n)] for _ in range(kk)]
    for i in range(0, n):
        for j in range(0, kk):
            for k in range(0, m):
                print(f'i={i}, j={j}, k={kk}')
                c[i][j] += (a[i][k] * b[k][j]) % mod
            c[i][j] %= mod
    print(c)
    return c


def test():
    fib_matrix = [
        [1, 1],
        [1, 0]
    ]
    fib_first = [
        [1, 0]
    ]
    f1 = 1
    f0 = 0
    mod = 10000

    for i in range(1, 10):
        print(f'F({i}) = {fib_first[0][0]}')
        fib_first = matrix_mul(fib_first, fib_matrix, mod)

        f2 = (f1 + f0) % mod
        f0 = f1
        f1 = f2



test()