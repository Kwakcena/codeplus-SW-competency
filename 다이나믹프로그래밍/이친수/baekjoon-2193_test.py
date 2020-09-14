from pprint import pprint


def test_solution():
    assert solution(5) == 5
    assert solution(4) == 3
    assert solution(3) == 2
    assert solution(2) == 1
    assert solution(1) == 1


def solution(n):
    dp = [[0] * 2 for _ in range(n + 1)]

    dp[0][1] = 1
    dp[0][0] = 0
    for i in range(1, n):
        dp[i][1] = dp[i - 1][0]
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

    return sum(dp[n - 1])


n = int(input())
print(solution(n))
