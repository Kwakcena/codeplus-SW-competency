dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def go(y, x):
    ans = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
            index = ord(board[ny][nx]) - 65
            if not check[index]:
                check[index] = True
                next = go(ny, nx)
                ans = max(ans, next)
                check[index] = False
    return ans + 1


r, c = map(int, input().split())
board = [input() for _ in range(r)]
check = [False] * 26
check[ord(board[0][0]) - 65] = True
print(go(0, 0))
