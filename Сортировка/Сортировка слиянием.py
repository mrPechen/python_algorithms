# Сложность O(n*log(n))
#память O()
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr) // 2
    left = arr[:n]
    right = arr[n:]
    merge_sort(left)
    merge_sort(right)

    left_index = 0
    right_index = 0
    len_arr_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[len_arr_index] = left[left_index]
            left_index += 1
        else:
            arr[len_arr_index] = right[right_index]
            right_index += 1
        len_arr_index += 1

    while left_index < len(left):
        arr[len_arr_index] = left[left_index]
        left_index += 1
        len_arr_index += 1
    while right_index < len(right):
        arr[len_arr_index] = right[right_index]
        right_index += 1
        len_arr_index += 1
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    print(f"массив = {arr}")
    arr_copy = arr
    first = merge_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(first == second)


test()