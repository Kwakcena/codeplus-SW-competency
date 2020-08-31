mod = 10 ** 9 + 9
limit = 10 ** 5
dp = [[0] * 4 for _ in range(limit + 1)]

for i in range(1, limit + 1):
    if i - 1 >= 0:
        dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
        if i == 1:
            dp[i][1] = 1
    if i - 2 >= 0:
        dp[i][2] = dp[i - 2][1] + dp[i - 2][3]
        if i == 2:
            dp[i][2] = 1
    if i - 3 >= 0:
        dp[i][3] = dp[i - 3][1] + dp[i - 3][2]
        if i == 3:
            dp[i][3] = 1

    dp[i][1] %= mod
    dp[i][2] %= mod
    dp[i][3] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % mod)
