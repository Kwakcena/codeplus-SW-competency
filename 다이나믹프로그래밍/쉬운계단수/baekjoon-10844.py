n = int(input())
mod = 10 ** 9

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(10):
        if i == 1 and j != 0:
            dp[i][j] = 1
        else:
            if j - 1 >= 0 and j + 1 <= 9:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            if j + 1 == 10:
                dp[i][j] = dp[i - 1][j - 1]
            if j - 1 == -1:
                dp[i][j] = dp[i - 1][j + 1]
        dp[i][j] %= mod

print(sum(dp[n]) % mod)
