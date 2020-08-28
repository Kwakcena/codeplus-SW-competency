import sys
from functools import reduce
from collections import Counter

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n = int(input())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]


def dfs(y, x, num):
    visited[y][x] = num
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if visited[ny][nx] == -1 and field[ny][nx] == 1:
                dfs(ny, nx, num)


number = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1 and field[i][j] == 1:
            number += 1
            dfs(i, j, number)

answer = sorted(list(Counter(
    [i for i in reduce(lambda x, y: x + y, visited) if i > 0]).values()))
print(number)
print('\n'.join(map(str, answer)))