import sys
from collections import deque

dx = [-1, +1, 2]

def bfs(N, K, check):
    q = deque()

    time = 0
    q.append((N, time))
    check[N] = True

    while q:
        N, time = q.popleft()
        if N == K:
            return time
        for i in range(3):
            if i == 2:
                next = N * dx[i]
            else:
                next = N + dx[i]

            if 0 <= next < 100001:
                if not check[next]:
                    q.append((next, time + 1))
                    check[next] = True

def solution():
    N, K = map(int, sys.stdin.readline().split())
    check = [False] * 200001

    print(bfs(N, K, check))

solution()

