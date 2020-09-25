def solution(n, a):
    d = [0] * n
    v = [-1] * n

    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[i] > a[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                v[i] = j
    return [d, v]


def go(index, v, a):
    if index == -1:
        return
    go(v[index], v, a)
    print(a[index], end=' ')


n = int(input())
a = list(map(int, input().split()))

[longest, longest_list] = solution(n, a)

ans = max(longest)
index = [i for i, v in enumerate(longest) if v == ans][0]

print(ans)
go(index, longest_list, a)
