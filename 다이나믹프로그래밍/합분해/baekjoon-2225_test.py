from pprint import pprint


def test_solution():
    assert solution(20, 2) == 21


def solution(n, k):
    mod = 10 ** 9
    d = [[0] * (n + 1) for _ in range(k + 1)]
    pprint(d, indent=2, width=80)

    # 0부터 0까지의 정수 0개를 더해서 그 합이 0이 되는 경우의 수 = 1
    d[0][0] = 1
    for i in range(1, k + 1):
        for j in range(n + 1):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
        d[i][j] %= mod

    pprint(d, indent=2, width=80)

    return d[k][n]


n, k = map(int, input().split())
print(solution(n, k))
