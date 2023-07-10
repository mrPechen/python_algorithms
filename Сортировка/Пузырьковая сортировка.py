# Сложность O(n^2)
# память O(1)
import random


def bubble_sort(arr):
    for j in range(len(arr)):
        is_sorted = True
        for i in range(1, len(arr) - j):
            if arr[i] < arr[i-1]:
                is_sorted = False
                arr[i], arr[i-1] = arr[i-1], arr[i]
        if is_sorted:
            return arr



def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    print(f"массив = {arr}")
    arr_copy = arr
    first = bubble_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(first == second)


test()
