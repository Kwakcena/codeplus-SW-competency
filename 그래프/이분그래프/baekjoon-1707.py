import sys

sys.setrecursionlimit(10 ** 5)


def dfs(vertex, color, visited, adj_list):
    visited[vertex] = color
    for next in adj_list[vertex]:
        if visited[next] == 0:
            dfs(next, 3 - color, visited, adj_list)


def check(visited, adj_lists):
    for current_node, adj_list in enumerate(adj_lists):
        for next_node in adj_list:
            if visited[current_node] == visited[next_node]:
                return False
    return True


if __name__ == "__main__":
    test_case = int(sys.stdin.readline())
    while test_case:
        V, E = map(int, sys.stdin.readline().split())
        adj_list = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)

        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            adj_list[u].append(v)
            adj_list[v].append(u)

        for start in range(1, V + 1):
            if not visited[start]:
                dfs(start, 1, visited, adj_list)
        print("YES" if check(visited, adj_list) else "NO")

        test_case -= 1
