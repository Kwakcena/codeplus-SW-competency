n, m = map(int, input().split())
answer = [0] * m


def go(start, index):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for number in range(start, n + 1):
        answer[index] = number
        go(number, index + 1)


go(1, 0)
