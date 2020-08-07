def go(goal, max_ans_len, nums, max_index_range, index = 0, cnt = 0, ans = 0):
    if cnt == max_ans_len:
        if ans == goal:
            return 1
        else:
            return 0

    if index >= max_index_range:
        return 0

    return go(goal, max_ans_len, nums, max_index_range, index + 1, cnt + 1, ans + nums[index]) + \
           go(goal, max_ans_len, nums, max_index_range, index + 1, cnt, ans)


if __name__ == "__main__":
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = 0
    for i in range(1, n + 1):
        ans += go(s, i, nums, n, 0, 0, 0)
    print(ans)
