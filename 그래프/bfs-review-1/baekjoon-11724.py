import sys
sys.setrecursionlimit(10**5)

n, m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False] * (n + 1)


def dfs(x, num):
    visited[x] = num
    for y in adj_list[x]:
        if not visited[y]:
            dfs(y, num)


number = 0
for start in range(1, n + 1):
    if not visited[start]:
        number += 1
        dfs(start, number)

print(number)
