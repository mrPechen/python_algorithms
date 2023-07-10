"""
Часто используется вметсе с динамическим программированием.
Сожность O(n)
"""

def sliding_window():
    arr = [1, 7, 5, 3, 2, 3, 8, 9]
    k = 4 # количество используемых элементов в массиве
    sum = 0 # сумма К-элементов
    for i in range(k): #O(k)
        sum += arr[i]
    print(sum)
    for i in range(1, (len(arr) - k) + 1): # O(n)
        sum = sum - arr[i - 1] + arr[i + k - 1]
        print(sum)

sliding_window()