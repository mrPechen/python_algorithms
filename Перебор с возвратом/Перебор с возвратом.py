# в основном используется для подсчета вариантов чего нибудь. Например задача про 8 ферзей
# сложность O(n!)

def queens(row, col, diag_left, diag_right): # 8x8
    n = len(col)
    if row == n:
        return True
    count = 0
    for column in range(n):
        if col[column] == 0 and diag_left[column + row] == 0 and diag_right[row - column + (n - 1)] == 0:
            col[column], diag_left[column + row], diag_right[row - column + (n - 1)] = 1, 1, 1
            count += queens(row + 1, col, diag_left, diag_right)
            col[column], diag_left[column + row], diag_right[row - column + (n - 1)] = 0, 0, 0
    return count


def test():
    for n in range(1, 13):
        col = [int(0) for _ in range(n)]
        diag_left = [int(0) for _ in range(2 * n - 1)]
        diag_right = [int(0) for _ in range(2 * n - 1)]

        res = queens(0, col, diag_left, diag_right)
        print(f'В матрице {n}x{n} количество возможных вариантов = {res}')


test()