n = int(input())
mod = 10007

dp = [[1] * 10 for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            dp[i][j] %= mod
print(sum(dp[n]) % mod)
