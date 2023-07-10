# сложность O(n*log(n))
# память O(1)
import random


def partition(arr, i, j):
    pivot = i
    s1_index = i
    s2_index = i
    for k in range(i+1, j):
        if arr[k] >= arr[pivot]:
            s2_index += 1
        else:
            s1_index += 1
            arr[s1_index], arr[k] = arr[k], arr[s1_index]
            s2_index += 1
    arr[pivot], arr[s1_index] = arr[s1_index], arr[pivot]
    return s1_index


def pre_quick_sort(arr, i, j):
    if i == j:
        return
    pivot = partition(arr, i, j)
    pre_quick_sort(arr, i, pivot)
    pre_quick_sort(arr, pivot + 1, j)




def quick_sort(arr):
    pre_quick_sort(arr, 0, len(arr))
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    print(f"массив = {arr}")
    arr_copy = arr.copy()
    first = quick_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(second)
    print(first == second)


test()