def test_solution():
    assert solution(
        10,
        [10, -4, 3, 1, 5, 6, -35, 12, 21, -1],
    ) == 33


def solution(n, nums):
    dp = [0] * n

    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])

    return max(dp)


n = int(input())
nums = list(map(int, input().split()))
print(solution(n, nums))