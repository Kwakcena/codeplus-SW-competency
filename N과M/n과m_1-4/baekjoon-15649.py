n, m = map(int, input().split())
check = [False] * (n + 1)
answer = [0] * m


def go(index):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for number in range(1, n + 1):
        if check[number]:
            continue

        check[number] = True
        answer[index] = number
        go(index + 1)
        check[number] = False


go(0)
