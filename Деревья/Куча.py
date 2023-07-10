"""
Куча(mix heap) - это структура данных, которая основана на бинарном дереве.
У нее есть свойство, что сыновья каждой вершины должны быть больше, чем
их родитель.

Max heap - min heap наоборот.

Возможные операции:
1. Push (O(log(n)))
2. Pop (O(log(n)))
3. Top (O(1))
"""


def add(heap, x):
    heap.append(x)
    ind = len(heap) - 1
    while ind != 1 and heap[ind] < heap[int(ind / 2)]:
        heap[ind], heap[int(ind / 2)] = heap[int(ind / 2)], heap[ind]
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


def test():
    heap = [1]
    add(heap, 2)
    add(heap, 5)
    add(heap, 3)
    add(heap, 10)
    add(heap, 6)
    add(heap, 9)
    add(heap, 5)
    add(heap, 12)
    add(heap, 40)

    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))
    erase(heap)
    print(top(heap))

test()