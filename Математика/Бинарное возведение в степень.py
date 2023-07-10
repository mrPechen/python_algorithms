#сложность O(log(n))
def bin_pow1(a, n):
    if n == 0:
        return True
    if n % 2 == 1:
        return bin_pow1(a, n - 1) * a
    b = bin_pow1(a, n / 2)
    return b * b


def bin_pow2(a, n):
    res = 1
    while n != 0:
        if n & 1:
            res *= a
        n >>= 1
        a *= a
    return res


def test():
    print(bin_pow1(2, 10) == 1024)
    print(bin_pow1(3, 5) == 243)
    print(bin_pow1(3, 15) == 14348907)
    print(bin_pow2(2, 10) == 1024)
    print(bin_pow2(3, 5) == 243)
    print(bin_pow2(3, 15) == 14348907)

test()