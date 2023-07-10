import random
# Сложность O(n * log(n))


def add(heap, x):
    heap.append(x)
    ind = len(heap) - 1
    while ind != 1 and heap[int(ind)] < heap[int(ind / 2)]:
        heap[int(ind)], heap[int(ind / 2)] = heap[int(ind / 2)], heap[int(ind)]
        ind /= 2


def erase(heap):
    heap[1], heap[len(heap)-1] = heap[len(heap)-1], heap[1]
    heap.pop(-1)
    ind = 1
    while ind * 2 < len(heap) and heap[ind] > heap[ind*2] or ind * 2 + 1 < len(heap) and heap[ind] > heap[ind*2+1]:
        if ind * 2 + 1 >= len(heap) or heap[ind*2] < heap[ind*2+1]:
            heap[ind], heap[ind*2] = heap[ind*2], heap[ind]
            ind *= 2
        else:
            heap[ind], heap[ind*2+1] = heap[ind*2+1], heap[ind]
            ind *= 2
            ind += 1


def top(heap):
    return heap[1]


def empty(heap):
    return len(heap) == 1


def heap_sort(arr):
    heap = [1]
    for i in range(len(arr)):
        add(heap, arr[i])
    arr.clear()
    while not empty(heap):
        arr.append(top(heap))
        erase(heap)
    return arr


def test():
    arr = []
    n = random.randint(0, 10)
    for i in range(n):
        arr.append(random.randint(0, 10))
    print(f"массив = {arr}")
    arr_copy = arr.copy()
    first = heap_sort(arr)
    second = sorted(arr_copy)
    print(first)
    print(second)
    print(first == second)


test()