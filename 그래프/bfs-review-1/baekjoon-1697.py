import sys
from collections import deque

MAX = 10 ** 5 + 1
n, k = map(int, sys.stdin.readline().split())
dist = [-1] * MAX

q = deque()
q.append(n)
dist[n] = 0

while q:
    now = q.popleft()
    for next in [now-1, now+1, now*2]:
        if 0 <= next < MAX:
            if dist[next] == -1:
                q.append(next)
                dist[next] = dist[now] + 1

print(dist[k])


