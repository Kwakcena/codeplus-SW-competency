def solution(n, a):
    d = [0] * n

    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[i] > a[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)


n = int(input())
a = list(map(int, input().split()))[::-1]

print(solution(n, a))