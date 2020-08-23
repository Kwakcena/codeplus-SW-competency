import sys
from collections import deque


def bfs(N, K, check):
    q = deque()
    q.append((N, 0))
    check[N] = True

    while q:
        N, time = q.popleft()
        if N == K:
            return time
        for next in [N - 1, N + 1, N * 2]:
            if 0 <= next < 100001 and not check[next]:
                q.append((next, time + 1))
                check[next] = True


def solution():
    N, K = map(int, sys.stdin.readline().split())
    check = [False] * 200001

    print(bfs(N, K, check))


solution()
