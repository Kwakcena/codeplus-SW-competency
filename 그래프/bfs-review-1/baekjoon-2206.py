import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
dist = [[[-1] * 2 for i in range(m)] for j in range(n)]

dist[0][0][0] = 1
q = deque()
q.append((0, 0, 0))

while q:
    y, x, wall = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if field[ny][nx] == 0 and dist[ny][nx][wall] == -1:
                q.append((ny, nx, wall))
                dist[ny][nx][wall] = dist[y][x][wall] + 1
            if wall == 0 and field[ny][nx] == 1 and dist[ny][nx][
                wall + 1] == -1:
                q.append((ny, nx, wall + 1))
                dist[ny][nx][wall + 1] = dist[y][x][wall] + 1

if dist[n - 1][m - 1][0] != -1 and dist[n - 1][m - 1][1] != -1:
    print(min(dist[n - 1][m - 1]))
elif dist[n - 1][m - 1][0] != -1:
    print(dist[n - 1][m - 1][0])
elif dist[n - 1][m - 1][1] != -1:
    print(dist[n - 1][m - 1][1])
else:
    print(-1)
