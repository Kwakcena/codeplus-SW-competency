import sys
sys.setrecursionlimit(10**6)

dy, dx = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    field = [list(map(int, input().split())) for _ in range(h)]
    check = [[0] * w for _ in range(h)]

    def dfs(y, x, land):
        check[y][x] = land
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if check[ny][nx] == 0 and field[ny][nx] == 1:
                    dfs(ny, nx, land)

    number = 0
    for i in range(h):
        for j in range(w):
            if check[i][j] == 0 and field[i][j] == 1:
                number += 1
                dfs(i, j, number)
    print(number)
