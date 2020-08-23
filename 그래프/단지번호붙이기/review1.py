import sys
from functools import reduce
from collections import Counter, deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, color):
    visited[y][x] = color
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                dfs(ny, nx, color)


def bfs(y, x, color):
    q = deque()
    q.append((y, x))
    visited[y][x] = color

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0 and graph[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = color


color = 0
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0 and graph[y][x] == 1:
            color += 1
            # dfs(y, x, color)
            bfs(y, x, color)

answer = reduce(lambda x, y: x + y, visited)
answer = [x for x in answer if x > 0]
answer = sorted(list(Counter(answer).values()))

print(color)
print('\n'.join(map(str, answer)))
