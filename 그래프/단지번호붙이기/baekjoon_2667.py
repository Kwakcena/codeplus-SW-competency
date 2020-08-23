import sys
from collections import Counter, deque
from functools import reduce

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 둘의 차이점?
# visited = [[0] * N] * N
visited = [[0 for _ in range(N)] for _ in range(N)]
address_number = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, number):
    visited[y][x] = number
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if N > new_x >= 0 and N > new_y >= 0:
            if field[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                dfs(new_y, new_x, number)


def bfs(y, x, number):
    q = deque()
    q.append((y, x))
    visited[y][x] = number

    while q:
        y, x = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if N > new_x >= 0 and N > new_y >= 0:
                if field[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                    q.append((new_y, new_x))
                    visited[new_y][new_x] = number


for y in range(N):
    for x in range(N):
        if field[y][x] == 1 and visited[y][x] == 0:
            address_number += 1
            # dfs(y, x, address_number)
            bfs(y, x, address_number)

ans = reduce(lambda x, y: x + y, visited)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(address_number)
print('\n'.join(map(str, ans)))
