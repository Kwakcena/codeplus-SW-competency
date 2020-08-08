max, min = -10 ** 10, 10 ** 10

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

def go(nums, index, cur, plus, minus, mul, div):
    global min, max
    # answer
    if index == n:
        if min > cur:
            min = cur
        if max < cur:
            max = cur
        return

    # impossible
    if index > n:
        return

    # next
    if plus > 0:
        go(nums, index + 1, cur + nums[index], plus - 1, minus, mul, div)
    if minus > 0:
        go(nums, index + 1, cur - nums[index], plus, minus - 1, mul, div)
    if mul > 0:
        go(nums, index + 1, cur * nums[index], plus, minus, mul - 1, div)
    if div > 0:
        if cur < 0:
            go(nums, index + 1, -(-cur // nums[index]), plus, minus, mul, div - 1)
        else:
            go(nums, index + 1, cur // nums[index], plus, minus, mul, div - 1)


go(nums, 1, nums[0], plus, minus, mul, div)

print(max)
print(min)
