import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 가로, 세로
M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[-1] * M for _ in range(N)]


def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                check[i][j] = 0
                q.append((i, j))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if tomato[ny][nx] == 0 and check[ny][nx] == -1:
                    q.append((ny, nx))
                    check[ny][nx] = check[y][x] + 1


bfs()
ans = max([max(row) for row in check])
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 and check[i][j] == -1:
            ans = -1

print(ans)
