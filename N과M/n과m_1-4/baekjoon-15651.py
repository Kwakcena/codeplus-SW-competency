n, m = map(int, input().split())
answer = [0] * m
check = [False] * (n + 1)

def go(index):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for number in range(1, n + 1):
        answer[index] = number
        go(index + 1)

go(0)