n, m = map(int, input().split())
# 2차원 배열 입력받는 방법
board = [list(map(int, input().split())) for _ in range(n)]

max = 0

for i in range(n):
    for j in range(m):
        if j + 3 < m:
            temp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][
                j + 3]
            if temp > max:
                max = temp
        if i + 3 < n:
            temp = board[i][j] + board[i + 1][j] + board[i + 2][j] + \
                   board[i + 3][j]
            if temp > max:
                max = temp
        if i + 1 < n and j + 2 < m:
            temp = board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + \
                   board[i + 1][j + 2]
            if temp > max:
                max = temp
        if i + 2 < n and j + 1 < m:
            temp = board[i][j] + board[i][j + 1] + board[i + 1][j] + \
                   board[i + 2][j]
            if temp > max:
                max = temp
        if i + 1 < n and j + 2 < m:
            temp = board[i][j] + board[i][j + 1] + board[i][j + 2] + \
                   board[i + 1][j + 2]
            if temp > max:
                max = temp
        if i + 2 < n and j - 1 >= 0:
            temp = board[i][j] + board[i + 1][j] + board[i + 2][j] + \
                   board[i + 2][j - 1]
            if temp > max:
                max = temp
        if i - 1 >= 0 and j + 2 < m:
            temp = board[i][j] + board[i][j + 1] + board[i][j + 2] + \
                   board[i - 1][j + 2]
            if temp > max:
                max = temp
        if i + 2 < n and j + 1 < m:
            temp = board[i][j] + board[i + 1][j] + board[i + 2][j] + \
                   board[i + 2][j + 1]
            if temp > max:
                max = temp
        if i + 1 < n and j + 2 < m:
            temp = board[i][j] + board[i][j + 1] + board[i][j + 2] + \
                   board[i + 1][j]
            if temp > max:
                max = temp
        if i + 2 < n and j + 1 < m:
            temp = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + \
                   board[i + 2][j + 1]
            if temp > max:
                max = temp
        if i + 1 < n and j + 1 < m:
            temp = board[i][j] + board[i + 1][j] + board[i][j + 1] + \
                   board[i + 1][j + 1]
            if temp > max:
                max = temp
        if i - 1 >= 0 and j + 2 < m:
            temp = board[i][j] + board[i][j + 1] + board[i - 1][j + 1] + \
                   board[i - 1][j + 2]
            if temp > max:
                max = temp
        if i + 2 < n and j + 1 < m:
            temp = board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + \
                   board[i + 2][j + 1]
            if temp > max:
                max = temp
        if i + 1 < n and j + 2 < m:
            temp = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + \
                   board[i + 1][j + 2]
            if temp > max:
                max = temp
        if i + 2 < n and j - 1 >= 0:
            temp = board[i][j] + board[i + 1][j] + board[i + 1][j - 1] + \
                   board[i + 2][j - 1]
            if temp > max:
                max = temp

        if j + 2 < m:
            temp = board[i][j] + board[i][j + 1] + board[i][j + 2]
            if i - 1 >= 0:
                temp2 = temp + board[i - 1][j + 1]
                if temp2 > max:
                    max = temp2

            if i + 1 < n:
                temp2 = temp + board[i + 1][j + 1]
                if temp2 > max:
                    max = temp2

        if i + 2 < n:
            temp = board[i][j] + board[i + 1][j] + board[i + 2][j]
            if j + 1 < m:
                temp2 = temp + board[i + 1][j + 1]
                if temp2 > max:
                    max = temp2

            if j - 1 >= 0:
                temp2 = temp + board[i + 1][j - 1]
                if temp2 > max:
                    max = temp2


print(max)
