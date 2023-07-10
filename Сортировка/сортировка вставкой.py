# сложность O(n^2)
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i-1
        while j >= 0 and arr[j] > cur:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = cur
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    print(f"массив = {arr}")
    arr_copy = arr
    first = insertion_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(first == second)

test()