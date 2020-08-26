import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline())

for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [0] * (n + 1)


    def dfs(x, color):
        visited[x] = color
        for next in adj_list[x]:
            if visited[next] == 0:
                if not dfs(next, 3 - color):
                    return False
            elif visited[next] == visited[x]:
                return False
        return True


    color = 1
    ans = True
    for start in range(1, n + 1):
        if visited[start] == 0:
            if not dfs(start, color):
                ans = False
    print("YES" if ans else "NO")
