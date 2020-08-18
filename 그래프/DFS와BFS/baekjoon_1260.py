import sys
from collections import deque


def input(graph, m):
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    for vertexs in graph:
        vertexs.sort()


def dfs(graph, x, check):
    check[x] = True
    print(x, end=' ')
    for vertex in graph[x]:
        if not check[vertex]:
            dfs(graph, vertex, check)


def bfs(graph, start, check):
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in graph[x]:
            if not check[y]:
                check[y] = True
                q.append(y)


if __name__ == "__main__":
    n, m, start = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    input(graph, m)
    dfs(graph, start, [False] * (n + 1))
    print()
    bfs(graph, start, [False] * (n + 1))
