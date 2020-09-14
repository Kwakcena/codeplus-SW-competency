def test_solution():
    assert solution(5, [
        [50, 10, 100, 20, 40],
        [30, 50, 70, 10, 60],
    ]) == 260

    assert solution(7, [
        [10, 30, 10, 50, 100, 20, 40],
        [20, 40, 30, 50, 60, 20, 80],
    ]) == 290

    assert solution(1, [
        [10],
        [20],
    ]) == 20

    assert solution(2, [
        [10, 100],
        [20, 50],
    ]) == 120


def solution(n, stickies):
    if n == 1:
        return max(stickies[0][0], stickies[1][0])

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = stickies[0][0]
    dp[1][0] = stickies[1][0]

    dp[0][1] = dp[1][0] + stickies[0][1]
    dp[1][1] = dp[0][0] + stickies[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickies[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickies[1][i]

    return max(dp[0][n - 1], dp[1][n - 1])


t = int(input())
for _ in range(t):
    n = int(input())
    stickies = [list(map(int, input().split())) for _ in range(2)]

    print(solution(n, stickies))