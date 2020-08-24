import sys
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def find_process(q, R, C, water):
    goal_y, goal_x = 0, 0
    start_y, start_x = 0, 0

    for i in range(R):
        for j in range(C):
            if a[i][j] == '*':
                q.append((i, j))
                water[i][j] = 0
            elif a[i][j] == 'D':
                goal_y, goal_x = i, j
            elif a[i][j] == 'S':
                start_y, start_x = i, j

    return goal_y, goal_x, start_y, start_x


# 물이 퍼지는 시간
def bfs_water(q, R, C, water):
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if a[ny][nx] != 'D' and a[ny][nx] != 'X' and water[ny][
                    nx] == -1:
                    q.append((ny, nx))
                    water[ny][nx] = water[y][x] + 1


def bfs_dist(q, R, C, sy, sx, water):
    dist = [[-1] * C for _ in range(R)]
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if dist[ny][nx] != -1 or a[ny][nx] == 'X':
                    continue
                if water[ny][nx] == -1 or dist[y][x] + 1 < water[ny][nx]:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
    return dist


def answer(dist, ey, ex):
    if dist[ey][ex] == -1:
        print('KAKTUS')
    else:
        print(dist[ey][ex])


if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    a = [list(sys.stdin.readline().strip()) for _ in range(R)]
    water = [[-1] * C for _ in range(R)]

    q = deque()
    ey, ex, sy, sx = find_process(q, R, C, water)
    bfs_water(q, R, C, water)
    dist = bfs_dist(q, R, C, sy, sx, water)
    answer(dist, ey, ex)
