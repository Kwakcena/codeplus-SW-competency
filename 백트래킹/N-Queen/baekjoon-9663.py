def check(row, col):
    # (row, col) 위치로부터 위 방향
    for i in range(n):
        if i == row:
            continue
        if a[i][col]:
            return False
    y = row - 1
    x = col - 1
    # (row, col) 위치에서 왼쪽 위 대각선
    while y >= 0 and x >= 0:
        if a[y][x]:
            return False
        y -= 1
        x -= 1

    # (row, col) 위치에서 오른쪽 위 대각선
    y = row - 1
    x = col + 1
    while y >= 0 and x < n:
        if a[y][x]:
            return False
        y -= 1
        x += 1
    return True


def calc(row):
    if row == n:
        global ans
        ans += 1
        return
    for col in range(n):
        a[row][col] = True
        if check(row, col):
            calc(row + 1)
        a[row][col] = False


n = int(input())
ans = 0
a = [[False] * n for _ in range(n)]
calc(0)
print(ans)
