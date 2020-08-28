import sys
from collections import deque

q = deque()
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
r, c = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().strip() for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
water = [[-1] * c for _ in range(r)]

sy, sx = 0, 0
ey, ex = 0, 0

for i in range(r):
    for j in range(c):
        if field[i][j] == '*':
            q.append((i, j))
            water[i][j] = 0
        elif field[i][j] == 'S':
            sy, sx = i, j
            dist[i][j] = 0
        elif field[i][j] == 'D':
            ey, ex = i, j

while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if field[ny][nx] != 'D' and field[ny][nx] != 'X' and water[ny][nx] == -1:
                q.append((ny, nx))
                water[ny][nx] = water[y][x] + 1

q.append((sy, sx))
while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if dist[ny][nx] != -1 or field[ny][nx] == 'X':
                continue
            if dist[y][x] + 1 < water[ny][nx] or water[ny][nx] == -1:
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1

if dist[ey][ex] == -1:
    print("KAKTUS")
else:
    print(dist[ey][ex])