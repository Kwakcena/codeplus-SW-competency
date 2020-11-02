def calc(first, second):
    t1, t2 = 0, 0
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j:
                continue
            t1 += s[first[i]][first[j]]
            t2 += s[second[i]][second[j]]
    diff = abs(t1 - t2)
    return diff


def go(index, first, second):
    if index == n:
        if len(first) > n // 2:
            return -1
        if len(second) > n // 2:
            return -1
        return calc(first, second)

    ans = -1
    first.append(index)
    t1 = go(index + 1, first, second)

    if ans == -1 or (t1 != -1 and t1 < ans):
        ans = t1
    first.pop()

    second.append(index)
    t2 = go(index + 1, first, second)

    if ans == -1 or (t2 != -1 and t2 < ans):
        ans = t2
    second.pop()

    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))
