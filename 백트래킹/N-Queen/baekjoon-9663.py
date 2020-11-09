col = [True] * 15
dig1 = [True] * 40
dig2 = [True] * 40


def calc(r):
    if r == N:
        return 1

    cnt = 0
    for c in range(N):
        if col[c] and dig1[r + c] and dig2[r - c + N]:
            col[c] = dig1[r + c] = dig2[r - c + N] = False
            cnt += calc(r + 1)
            col[c] = dig1[r + c] = dig2[r - c + N] = True

    return cnt


N = int(input())
print(calc(0))
