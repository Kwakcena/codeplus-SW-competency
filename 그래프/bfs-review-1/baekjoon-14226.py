from collections import deque

goal = int(input())

dist = [[-1] * (goal + 1) for _ in range(goal + 1)]
q = deque()
q.append((1, 0))
dist[1][0] = 0

while q:
    s, c = q.popleft()
    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    if dist[s][s] == -1:
        q.append((s, s))
        dist[s][s] = dist[s][c] + 1

    # 클립보등 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if s + c < goal + 1 and dist[s + c][c] == -1:
        q.append((s + c, c))
        dist[s + c][c] = dist[s][c] + 1

    # 화면에 있는 이모티콘 중 하나를 삭제한다.
    if s - 1 >= 2 and dist[s - 1][c] == -1:
        q.append((s - 1, c))
        dist[s - 1][c] = dist[s][c] + 1

print(min([i for i in dist[goal] if i > 0]))
