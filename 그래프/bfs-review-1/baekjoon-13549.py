from collections import deque

MAX = 10**5 + 1

n, k = map(int, input().split())
dist = [-1] * MAX

dist[n] = 0
q = deque()
q.append(n)

while q:
    now = q.popleft()

    if now * 2 < MAX and dist[now * 2] == -1:
        q.appendleft(now * 2)
        dist[now * 2] = dist[now]

    if now - 1 >= 0 and dist[now - 1] == -1:
        q.append(now - 1)
        dist[now - 1] = dist[now] + 1

    if now + 1 < MAX and dist[now + 1] == -1:
        q.append(now + 1)
        dist[now + 1] = dist[now] + 1

print(dist[k])