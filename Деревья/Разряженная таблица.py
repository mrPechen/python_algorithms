"""
Разряженная таблица - это структура данных, которая позволяет отвечать на запросы
на диапазоне. Работает за O(log(n)). часто используют при нахождении min и max
на отрезке потому что можно получить сложность O(1). Однако минус в том, что
в этой структуре данных мы не можем изменять массив.
"""
from math import log2


def test():
    a = [1, 2, 3, 4, 5, 6, 7, 8]

    st = [[int(0) for _ in range(int(log2(len(a))))] for _ in range(len(a) + 1)]

    for i in range(len(a)):
        st[i][0] = a[i]

    for j in range(1, len(st[0])):
        for i in range(len(a)):
            if i + (1 << (j-1)) < len(a):
                st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])

    l = 1
    r = 5
    j = int(log2(r - 1 + 1))
    print(min(st[l][j], st[r - (1 << j) + 1][j]))

test()