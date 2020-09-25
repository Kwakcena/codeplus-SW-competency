def solution(n, a):
    d = [0] * n

    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[i] > a[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return d


n = int(input())
a = list(map(int, input().split()))

reverse_a = a[::-1]

d1 = solution(n, a)
d2 = solution(n, reverse_a)[::-1]

ans = max([sum(value) - 1 for value in zip(d1, d2)])
print(ans)

