def test_solution():
    assert solution(6, [6, 10, 13, 9, 8, 1]) == 33


def test_solution2():
    assert solution2(6, [6, 10, 13, 9, 8, 1]) == 33


def solution(n, wines):
    dp = [[0] * 3 for _ in range(n)]

    dp[0][1] = wines[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = dp[i - 1][0] + wines[i]
        dp[i][2] = dp[i - 1][1] + wines[i]

    return max(dp[n - 1])


def solution2(n, wines):
    dp = [0] * (n + 1)
    wines = [0] + wines

    dp[1] = wines[1]
    if n >= 2:
        dp[2] = wines[1] + wines[2]
    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + wines[i],
            dp[i - 3] + wines[i - 1] + wines[i]
        )

    return dp[n]


n = int(input())
a = [int(input()) for _ in range(n)]
print(solution(n, a))