def bin_pow(a, n, mod):
    res = 1
    while n:
        if n & 1:
            res *= a
            res %= mod
        n >>= 1
        a *= a
        a %= mod
    return res


def test():
    mod = 1000000007
    print(2 * bin_pow(5, mod - 2, mod) % mod)

test()
