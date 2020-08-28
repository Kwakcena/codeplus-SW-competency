import sys
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
check = [[0] * m for _ in range(n)]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    check[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if check[ny][nx] == 0 and field[ny][nx] == 1:
                    q.append((ny, nx))
                    check[ny][nx] = check[y][x] + 1


bfs(0, 0)
print(check[n - 1][m - 1])
