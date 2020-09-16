def test_solution():
    assert solution(6, [10, 20, 10, 30, 20, 50]) == 4


def test_dp():
    assert dp(6, [10, 20, 10, 30, 20, 50]) == [1, 2, 1, 3, 2, 4]


def dp(n, a):
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[i] > a[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    return dp


def solution(n, a):
    return max(dp(n, a))


n = int(input())
a = list(map(int, input().split()))
print(solution(n, a))
