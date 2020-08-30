n, m = map(int, input().split())
check = [False] * (n + 1)
answer = [0] * m


def go(index, start):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for number in range(start, n + 1):
        answer[index] = number
        go(index + 1, number + 1)


go(0, 1)
