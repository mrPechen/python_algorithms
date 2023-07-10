# сложность O(n^2)
# память O(1)
import random


def selection_sort(arr):
    for j in range(len(arr)):
        min_index = j
        for i in range(j+1, len(arr)):
            if arr[min_index] > arr[i]:
                min_index = i
        arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    print(f"массив = {arr}")
    arr_copy = arr
    first = selection_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(first == second)



test()