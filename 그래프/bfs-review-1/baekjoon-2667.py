import sys

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n = int(input())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]


def dfs(y, x, num):
    visited[y][x] = num
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < 0:
            if visited[ny][nx] == -1 and field[ny][nx] == 1:
                dfs(ny, nx, num)


color = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and field[i][j] == 1:
            color += 1
            dfs(i, j, color)

print(color)
