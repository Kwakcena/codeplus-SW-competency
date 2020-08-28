import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

adj_list = [sorted(adj) for adj in adj_list]


def dfs(x, visited):
    visited[x] = True
    print(x, end=' ')
    for y in adj_list[x]:
        if not visited[y]:
            dfs(y, visited)


def bfs(x, visited):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        now = q.popleft()
        print(now, end=' ')

        for next in adj_list[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True


dfs(start, [False] * (n + 1))
print()
bfs(start, [False] * (n + 1))
