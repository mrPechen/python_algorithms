"""
Используется в основном для разбиение задачи на мелкие подзадачи, для задач связанных
с оптимизацией ( из пункта А в Б, числа Фибоначи)
Сложность O(n * k)
Память O(n)
"""


def dynamic_programming():
    n = int(input()) # кол-во ступенек
    k = int(input()) # ноличество ступенек за 1 прыжок

    arr = [1]
    for i in range(1, n):
        temp = 0
        for j in range(k):
            if len(arr) < 1 + j:
                break
            temp += arr[len(arr) - 1 - j]
        arr.append(temp)

    for i in range(n):
        print(arr[i])

dynamic_programming()