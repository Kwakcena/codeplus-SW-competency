import sys
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
check = [[[0] * 2 for j in range(m)] for i in range(n)]

q = deque()
q.append((0, 0, 0))
check[0][0][0] = 1

while q:
    y, x, wall = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            # 갈 수 있는 길이고, 벽돌을 깨서 가든 안깨서 가든 가본적 없다면,
            if field[ny][nx] == 0 and check[ny][nx][wall] == 0:
                # 이전 길에 1을 더한다.
                check[ny][nx][wall] = check[y][x][wall] + 1
                q.append((ny, nx, wall))
            # 한 번도 벽돌은 꺤적이 없고, 벽이며, 벽돌을 깨서 방문한 적 없는 곳이라면
            if wall == 0 and field[ny][nx] == 1 and check[ny][nx][
                wall + 1] == 0:
                # 이전 길에 1을 더한값을 벽돌을 깨서 간 정점에 추가한다.
                check[ny][nx][wall + 1] = check[y][x][wall] + 1
                q.append((ny, nx, wall + 1))

if check[n - 1][m - 1][0] != 0 and check[n - 1][m - 1][1] != 0: 
    # 벽을 깨고 도착한 길과 안꺠고 도착한 길 둘 다 존재하면 그중 작은 값을 답으로 출력한다.
    print(min(check[n - 1][m - 1]))
elif check[n - 1][m - 1][0] != 0:
    print(check[n - 1][m - 1][0])
elif check[n - 1][m - 1][1] != 0:
    print(check[n - 1][m - 1][1])
else:
    print(-1)
