import sys

n, m = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)


def dfs(x, count, visited):
    visited[x] = True

    if count == 4:
        return True

    for y in adj_list[x]:
        if not visited[y]:
            if dfs(y, count + 1, visited):
                return True
            else:
                visited[y] = False
    return False


ans = False
for start in range(n):
    if dfs(start, 0, [False] * n):
        ans = True
        break
print(1 if ans else 0)
