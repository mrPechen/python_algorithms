#сложность O(n+range_length)
import random


def counting_sort(arr):
    min = arr[0]
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

    bucket = [0] * (max - min + 1)
    for i in range(len(arr)):
        index = arr[i] - min
        bucket[index] = (bucket[index] + 1)
    arr.clear()
    for i in range(len(bucket)):
        count = bucket[i]
        for j in range(count):
            arr.append(i+min)
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    arr_copy = arr
    first = counting_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(first == second)


test()
