"""
SQRT-декомпозиция - это метод или структура данных, которая позволяет
некоторые типичные операции (например суммирование элементов на отрезке,
нахождение минимума и максимума) за сложность O(sqrt(n)).
"""
from math import sqrt


def test():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    s = sqrt(len(a))
    s += 1
    b = [int(0) for _ in range(int(s))]
    for i in range(len(a)):
        b[int(i / s)] += a[i]

    l = 1
    r = 6

    summ = 0

    for i in range(l, r + 1):
        if i % s == 0 and i + s - 1 <= r:
            summ += b[int(i / s)]
            i += s
        else:
            summ += a[i]

    print(summ)

test()
