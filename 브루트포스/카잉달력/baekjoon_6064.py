T = int(input())

answers = []
for _ in range(T):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    year = x
    for _ in range(n):
        if year % n == y:
            answers.append(year + 1)
            break
        year += m
    else:
        answers.append(-1)

for answer in answers:
    print(answer)