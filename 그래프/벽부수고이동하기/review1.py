import sys
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
check = [[[0] * 2 for j in range(m)] for i in range(n)]

q = deque()
q.append((0, 0, 0))
check[0][0][0] = 1

while q:
    y, x, wall = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if field[ny][nx] == 0 and check[ny][nx][wall] == 0:
                check[ny][nx][wall] = check[y][x][wall] + 1
                q.append((ny, nx, wall))
            if wall == 0 and field[ny][nx] == 1 and check[ny][nx][
                wall + 1] == 0:
                check[ny][nx][wall + 1] = check[y][x][wall] + 1
                q.append((ny, nx, wall + 1))

if check[n - 1][m - 1][0] != 0 and check[n - 1][m - 1][1] != 0:
    print(min(check[n - 1][m - 1]))
elif check[n - 1][m - 1][0] != 0:
    print(check[n - 1][m - 1][0])
elif check[n - 1][m - 1][1] != 0:
    print(check[n - 1][m - 1][1])
else:
    print(-1)
