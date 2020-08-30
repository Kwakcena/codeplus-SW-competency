import sys

n, m = map(int, sys.stdin.readline().split())
numbers = sorted(list(set(map(int, sys.stdin.readline().split()))))
n = len(numbers)
answer = [0] * m
used = [False] * n


def go(index):
    if index == m:
        sys.stdout.write(' '.join(map(str, answer)) + '\n')
        return

    for i in range(n):
        used[i] = True
        answer[index] = numbers[i]
        go(index + 1)
        used[i] = False

go(0)