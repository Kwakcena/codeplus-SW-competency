import sys
sys.setrecursionlimit(1000000)

test_case = int(sys.stdin.readline())

def dfs(x, adj_list, visited, color):
    visited[x] = color
    for y in adj_list[x]:
        if visited[y] == 0:
            if not dfs(y, adj_list, visited, 3 - color):
                return False
        elif visited[y] == visited[x]:
            return False
    return True


for _ in range(test_case):
    # vertex, edges = map(int, input().split())
    vertex, edges = map(int, sys.stdin.readline().split())
    visited = [0] * vertex
    adj_list = [[] for _ in range(vertex)]

    for i in range(edges):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    ans = True
    for start in range(vertex):
        if visited[start] == 0:
            if not dfs(start, adj_list, visited, 1):
                ans = False
    print("YES" if ans else "NO")
