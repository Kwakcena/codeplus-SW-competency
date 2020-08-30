n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answers = [0] * m
check = [False] * 10001

def go(index):
    if index == m:
        print(' '.join(map(str, answers)))
        return

    for number in numbers:
        if check[number]:
            continue

        check[number] = True
        answers[index] = number
        go(index + 1)
        check[number] = False


go(0)
