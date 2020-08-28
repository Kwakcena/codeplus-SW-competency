import sys
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
m, n = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[-1] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            q.append((i, j))
            check[i][j] = 0

while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if field[ny][nx] == 0 and check[ny][nx] == -1:
                q.append((ny, nx))
                check[ny][nx] = check[y][x] + 1

ans = max([max(row) for row in check])
for i in range(n):
    for j in range(m):
        if field[i][j] == 0 and check[i][j] == -1:
            ans = -1
print(ans)