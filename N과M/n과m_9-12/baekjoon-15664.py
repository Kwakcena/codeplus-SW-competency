n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
check = [False] * n
answer = [0] * m


def go(index, start):
    used = [False] * 10001
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n):
        if check[i] or used[numbers[i]]:
            continue

        check[i], used[numbers[i]] = True, True
        answer[index] = numbers[i]
        go(index + 1, i + 1)
        check[i] = False


go(0, 0)
