from collections import deque
from pprint import pprint

MAX = 200001
n, k = map(int, input().split())
dist = {}
q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        break

    if now - 1 >= 0 and now - 1 not in dist:
        q.append(now - 1)
        dist[now - 1] = now
    if now + 1 < MAX and now + 1 not in dist:
        q.append(now + 1)
        dist[now + 1] = now
    if now * 2 <= MAX and now * 2 not in dist:
        q.append(now * 2)
        dist[now * 2] = now


ans = []
start, end = k, n
while start != end:
    ans.append(start)
    start = dist[start]
ans.append(n)

print(len(ans) - 1)
print(' '.join(map(str, ans[::-1])))
