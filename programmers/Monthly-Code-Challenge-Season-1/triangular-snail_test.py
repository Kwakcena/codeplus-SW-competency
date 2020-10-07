from pprint import pprint


def test_solution():
    assert solution(4) == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
    assert solution(5) == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
    assert solution(6) == [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20,
                           12, 6, 7, 8, 9, 10, 11]


def solution(n):
    m = [[0] * n for _ in range(n)]

    v = 1
    r, c = 0, 0
    while n:
        for _ in range(n):
            m[r][c] = v
            v += 1
            r += 1
        n -= 1
        if not n:
            break

        r -= 1
        c += 1
        for _ in range(n):
            m[r][c] = v
            v += 1
            c += 1
        n -= 1
        if not n:
            break

        c -= 1
        for _ in range(n):
            r -= 1
            c -= 1
            m[r][c] = v
            v += 1
        n -= 1
        if not n:
            break

        r += 1

    pprint(m, indent=2, width=30)
    return list(filter(lambda x: x != 0, sum(m, [])))

# def solution(n):
#     dx = [0, 1, -1]
#     dy = [1, 0, -1]
#     b = [[0] * i for i in range(1, n + 1)]
#     x, y = 0, 0
#     num = 1
#     d = 0
#     while num <= (n + 1) * n // 2:
#         b[y][x] = num
#         ny = y + dy[d]
#         nx = x + dx[d]
#         num += 1
#         if 0 <= ny < n and 0 <= nx <= ny and b[ny][nx] == 0:
#             y, x = ny, nx
#         else:
#             d = (d + 1) % 3
#             y += dy[d]
#             x += dx[d]
#         pprint(b, indent=2, width=30)

    # return sum(b, [])
