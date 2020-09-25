def solution(n, a):
    d = [0] * n

    for i in range(len(a)):
        d[i] = a[i]
        for j in range(i):
            if a[i] > a[j] and d[j] + a[i] > d[i]:
                d[i] = d[j] + a[i]

    return max(d)


n = int(input())
a = list(map(int, input().split()))

print(solution(n, a))
