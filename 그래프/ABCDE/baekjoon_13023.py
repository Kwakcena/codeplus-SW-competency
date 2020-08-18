import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
answer = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(x, cnt, check):
    check[x] = True

    if cnt == 4:
        return 1

    res = 0
    for vertex in graph[x]:
        if not check[vertex]:
            res += dfs(vertex, cnt + 1, check)
            check[vertex] = False
    return res


for start in range(n):
    answer = dfs(start, 0, [False] * n)
    if answer > 0:
        break
print(1 if answer > 0 else 0)
