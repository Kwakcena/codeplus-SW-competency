def square(y, x):
    return (y // 3) * 3 + (x // 3)


def go(index):
    if index == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return

    y = index // n
    x = index % n

    if a[y][x] != 0:
        go(index + 1)
    else:
        for i in range(1, 10):
            if check_col[x][i] is False and check_row[y][i] is False and \
                    check_square[square(y, x)][i] is False:
                check_col[x][i] = check_row[y][i] = check_square[square(y, x)][
                    i] = True
                a[y][x] = i

                go(index + 1)

                check_col[x][i] = check_row[y][i] = check_square[square(y, x)][
                    i] = False
                a[y][x] = 0


n = 9
a = [list(map(int, input().split())) for _ in range(n)]

check_col = [[False] * 10 for _ in range(n)]
check_row = [[False] * 10 for _ in range(n)]
check_square = [[False] * 10 for _ in range(n)]

for row in range(n):
    for col in range(n):
        if a[row][col] != 0:
            check_col[col][a[row][col]] = True
            check_row[row][a[row][col]] = True
            check_square[square(row, col)][a[row][col]] = True

go(0)
