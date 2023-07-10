# этот алгоритм помогает найти все простые числа на отрезке от 1 до N

# память O(n), сложность O(n * log log(n))


def sieve(n):
    arr = [i for i in range(n + 1)]
    arr[1] = 0
    i = 2
    while i <= n:
        if arr[i] != 0: 
            j = i + i
            while j <= n:
                arr[j] = 0
                j = j + i
        i += 1
    arr = set(arr)
    arr.remove(0)
    return arr



def test():
    primes = sieve(100)
    for prime in primes:
        print(prime)

test()