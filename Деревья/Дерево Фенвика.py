"""
Дерево Фенквика - это структура данных, которая обладает следующими свойствами:

1. Позволяет вычислять значение некоторой обратимой операции G на любом отрезке
от L до R. Сложность O(log(n)).
2. Позволяет изменять значение конкретной переменной на индексе i.
Сложность O(log(n)).

Память O(n)
"""


n = 8 # длина массива а
tree = [int(0) for _ in range(n)]


def build_tree(a):
    for i in range(len(a)):
        update(i, a[i])


def get_sum1(r):
    result = 0
    r = r+1
    while r > 0:
        result += tree[r]
        r -= r & (-r)
    return result


def get_sum2(l, r):
    return get_sum1(r) - get_sum1(l-1)


def update(i, x):
    i += 1
    while i <= len(tree)-1:
        tree[i] += x
        i += i & (-i)


def test():
    a = [1, 2, 3, 4, 5, 6, 7, 8]

    build_tree(a)
    print(get_sum2(1, 6))
    update(3, 10)
    print(get_sum2(1, 6))


test()