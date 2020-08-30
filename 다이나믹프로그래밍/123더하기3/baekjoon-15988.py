mod = (10 ** 9) + 9
d = [0] * ((10 ** 6) + 1)
d[0], d[1], d[2] = 1, 1, 2

for i in range(3, 10 ** 6 + 1):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    d[i] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
