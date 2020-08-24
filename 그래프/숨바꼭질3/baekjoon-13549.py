from collections import deque

MAX = 200000


def bfs(n, k):
    dist = [-1] * MAX
    q, next_q = deque(), deque()
    q.append(n)
    dist[n] = 0

    while q:
        now = q.popleft()
        if now * 2 < MAX and dist[now * 2] == -1:
            dist[now * 2] = dist[now]
            q.append(now * 2)
        if now - 1 >= 0 and dist[now - 1] == -1:
            dist[now - 1] = dist[now] + 1
            next_q.append(now - 1)
        if now + 1 < MAX and dist[now + 1] == -1:
            dist[now + 1] = dist[now] + 1
            next_q.append(now + 1)
        if not q:
            q = next_q
            next_q = deque()

    return dist[k]
  

def solution(n, k):
    return bfs(n, k)


if __name__ == "__main__":
    n, k = map(int, input().split())
    answer = solution(n, k)

    print(answer)
