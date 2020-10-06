def test_solution():
    assert solution(11) == 3
    assert solution(7) == 4


def solution(n):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = i
        j = 1
        while j * j <= i:
            if d[i] > d[i - j * j] + 1:
                d[i] = d[i - j * j] + 1
            j += 1
    return d[n]


n = int(input())
print(solution(n))