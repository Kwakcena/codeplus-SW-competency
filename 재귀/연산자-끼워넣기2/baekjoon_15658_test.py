N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

def calculate(index, current, plus, minus, mul, div):
    if index == N:
        return (current, current)

    if index > N:
        return;

    res = []
    if plus > 0:
        res.append(calculate(index + 1, current + nums[index], plus - 1, minus, mul, div))
    if minus > 0:
        res.append(calculate(index + 1, current - nums[index], plus, minus - 1, mul, div))
    if mul > 0:
        res.append(calculate(index + 1, current * nums[index], plus, minus, mul - 1, div))
    if div > 0:
        if current > 0:
            res.append(calculate(index + 1, current // nums[index], plus, minus, mul, div - 1))
        else:
            res.append(calculate(index + 1, -( -current // nums[index]), plus, minus, mul, div- 1))

    return (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )

answer = calculate(1, nums[0], plus, minus, mul, div)
print(answer[0])
print(answer[1])