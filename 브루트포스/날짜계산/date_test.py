E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
year = 1

while True:
    if e == E and s == S and m == M:
        print(year)
        break
    if not e % 15:
        e = 1
    else:
        e += 1

    if not s % 28:
        s = 1
    else:
        s += 1

    if not m % 19:
        m = 1
    else:
        m += 1
    year += 1
