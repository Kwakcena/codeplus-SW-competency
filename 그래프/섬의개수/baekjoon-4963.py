from collections import deque

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(y, x, w, h, check, field, number):
    q = deque()
    q.append((y, x))
    check[y][x] = number

    while q:
        y, x = q.popleft()
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if field[ny][nx] == 1 and check[ny][nx] == -1:
                    q.append((ny, nx))
                    check[ny][nx] = number


if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        check = [[-1] * w for _ in range(h)]
        field = [list(map(int, input().split())) for _ in range(h)]
        number = 0
        for i in range(h):
            for j in range(w):
                if field[i][j] == 1 and check[i][j] == -1:
                    number += 1
                    bfs(i, j, w, h, check, field, number)
        if w == 0 and h == 0:
            break
        print(number)
