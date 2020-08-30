n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = [0] * m
check = [False] * n


def go(index):
    used = [False] * 10001
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(n):
        if check[i] or used[numbers[i]]:
            continue

        check[i] = True
        used[numbers[i]] = True
        answer[index] = numbers[i]
        go(index + 1)
        check[i] = False

go(0)
