n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
check = [False] * n
answer = [0] * m

def go(index, start):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n):
        if check[i]:
            continue

        check[i] = True
        answer[index] = numbers[i]
        go(index + 1, i + 1)
        check[i] = False

go(0, 0)