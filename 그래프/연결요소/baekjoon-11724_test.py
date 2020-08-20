import sys
sys.setrecursionlimit(100000)

def dfs(vertex, visited, adjacency_list):
    visited[vertex] = True
    for next_vertex in adjacency_list[vertex]:
        if not visited[next_vertex]:
            dfs(next_vertex, visited, adjacency_list)


def solution(n, adjacency_list):
    visited = [False] * (n + 1)
    answer = 0
    for start in range(1, n + 1):
        if not visited[start]:
            dfs(start, visited, adjacency_list)
            answer += 1

    return answer


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    adjacency_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    print(solution(n, adjacency_list))