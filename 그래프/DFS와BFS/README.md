# DFS와 BFS
DFS와 BFS의 목적은 임의의 정점 x에서 시작하여 모든 정점을 한번씩 방문하는 것이다.<br/>
다음과 같은 입력 조건에 대하여 DFS, BFS 코드를 작성 해 보자.

```python
# 정점 n, 간선 m
graph = [[] for _ in range(n + 1)] # 각 인덱스를 정점으로 하여 연결 관계를 표현하는 인접 리스트

# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 다음과 같이 입력이 들어오는 경우
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
```

## DFS - 깊이 우선 탐색
스택을 이용해서 갈 수 있는 만큼 최대한 많이 가는 방법. 갈 수 없다면 이전 정점으로 돌아온다.
```python
check = [False] * (n + 1)

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for v in graph[x]:
        if not check[v]:
            dfs(v)
```

## BFS - 너비 우선 탐색
큐를 이용해서 현재 위치에서 갈 수 있는 것을 모두 큐에 넣는 방식이다. 큐에 넣을 때 방문했다고 체크한다.
```python
from collections import deque

def bfs(x):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.leftpop()
        print(x, end=' ')
        for v in graph[x]:
            if not check[v]:
                check[v] = True
                q.append(v)
```