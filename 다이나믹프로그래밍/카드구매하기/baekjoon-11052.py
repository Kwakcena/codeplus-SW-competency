n = int(input())
card = [0] + list(map(int, input().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], card[j] + d[i - j])
print(d[n])