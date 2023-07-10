# сложность def euler = O(n*log(n)) или euler_fast = O(sqrt(n))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def euler(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count


def euler_fast(n):
    res = n
    prime = 2
    while n >= prime * prime:
        if n % prime == 0:
            res = res / prime * (prime - 1)
            while n % prime == 0:
                n /= prime
        prime += 1
    if n != 1:
        res = res / n * (n - 1)
    return res


def test():
    print(euler(9) == 6)
    print(euler_fast(9) == 6)

    print(euler(36) == 12)
    print(euler_fast(36) == 12)

test()
