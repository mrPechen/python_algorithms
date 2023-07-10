
def binary_search(arr, x):
    i = 0
    r = len(arr) - 1
    while i <= r:
        m = int((i + r) / 2)
        if arr[m] == x:
            return True
        if arr[m] < x:
            i = m + 1
            continue
        if arr[m] > x:
            r = m - 1
            continue
    return False


def test():
    arr = [1, 2, 4, 5, 7, 9, 12, 15, 19, 23]
    print(binary_search(arr, 7))
    print(binary_search(arr, 12))
    print(binary_search(arr, 23))
    print(binary_search(arr, 8))
    print(binary_search(arr, 3))
    print(binary_search(arr, -1))

test()