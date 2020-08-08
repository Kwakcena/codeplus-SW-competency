
def go(nums, index, cur, plus, minus, mul, div):
    # answer
    if index == len(nums):
        return (cur, cur)
    res = []

    # impossible
    if index > n:
        return

    # next
    if plus > 0:
        res.append(go(nums, index + 1, cur + nums[index], plus - 1, minus, mul, div))
    if minus > 0:
        res.append(go(nums, index + 1, cur - nums[index], plus, minus - 1, mul, div))
    if mul > 0:
        res.append(go(nums, index + 1, cur * nums[index], plus, minus, mul - 1, div))
    if div > 0:
        if cur < 0:
            res.append(go(nums, index + 1, -(-cur // nums[index]), plus, minus, mul, div - 1))
        else:
            res.append(go(nums, index + 1, cur // nums[index], plus, minus, mul, div - 1))
    ans = (max([t[0] for t in res]), min([t[1] for t in res]))
    return ans

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = go(nums, 1, nums[0], plus, minus, mul, div)

print(ans[0])
print(ans[1])
