#сложность O(n*d)
#память O(n)

import random


def radix_sort(arr):
    max_digits = max([len(str(x)) for x in arr])
    base = 10
    buckets = [[] for _ in range(base)]
    for pow in range(0, max_digits):
        for elem in arr:
            x = (elem // base ** pow) % base
            buckets[x].append(elem)
        arr.clear()
        arr = [i for j in buckets for i in j]
        buckets = [[] for _ in range(base)]
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 100))
    print(f"массив = {arr}")
    arr_copy = arr.copy()
    first = radix_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(second)
    print(first == second)


test()