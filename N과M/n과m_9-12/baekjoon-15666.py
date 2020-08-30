n, m = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))
n = len(numbers)
answer = [0] * m

def go(index, start):
    if index == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n):
        answer[index] = numbers[i]
        go(index + 1, i)

go(0, 0)
