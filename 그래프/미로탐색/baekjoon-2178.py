import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
check = [[False] * m for _ in range(n)]


def bfs(y, x):
    q = deque()
    check[y][x] = True
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if miro[ny][nx] == 1 and not check[ny][nx]:
                    q.append((ny, nx))
                    check[ny][nx] = True
                    miro[ny][nx] += miro[y][x]


bfs(0, 0)
print(miro[n - 1][m - 1])
