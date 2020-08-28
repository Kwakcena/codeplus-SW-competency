import sys
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
m, n = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if field[ny][nx] == 0 and dist[ny][nx] == -1:
                q.appendleft((ny, nx))
                dist[ny][nx] = dist[y][x]
            if field[ny][nx] == 1 and dist[ny][nx] == -1:
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
print(dist[n - 1][m - 1])
