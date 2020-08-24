import sys
from collections import deque

dy = [-1, +1, 0, 0]
dx = [0, 0, -1, +1]


def bfs(m, n, miro):
    q = deque()
    dist = [[-1] * m for _ in range(n)]
    q.append((0, 0))
    dist[0][0] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if miro[ny][nx] == 0 and dist[ny][nx] == -1:
                    q.appendleft((ny, nx))
                    dist[ny][nx] = dist[y][x]
                if miro[ny][nx] == 1 and dist[ny][nx] == -1:
                    q.append((ny, nx))
                    dist[ny][nx] = dist[y][x] + 1

    return dist[n - 1][m - 1]


def solution(m, n, miro):
    return bfs(m, n, miro)


if __name__ == "__main__":
    m, n = map(int, sys.stdin.readline().split())
    miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    answer = solution(m, n, miro)

    print(answer)
