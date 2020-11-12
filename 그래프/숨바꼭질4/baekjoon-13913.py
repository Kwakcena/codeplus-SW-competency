from collections import deque

MAX = 200001


def bfs(n, k):
    q = deque()
    q.append(n)
    dist = {}
    while q:
        now = q.popleft()
        if now == k:
            break

        for next in [now - 1, now + 1, now * 2]:
            if 0 <= next <= MAX and next not in dist:
                q.append(next)
                dist[next] = now
    return dist


def solution():
    n, k = map(int, input().split())
    move_dict = bfs(n, k)

    ans = []
    while k != n:
        ans.append(k)
        k = move_dict[k]
    ans.append(n)

    print(len(ans) - 1)
    print(' '.join(map(str, ans[::-1])))


solution()
