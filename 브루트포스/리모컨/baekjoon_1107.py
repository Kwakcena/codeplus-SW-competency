n = int(input())
m = int(input())
broken = [False] * 10

if m > 0:
    for button in list(map(int, input().split())):
        broken[button] = True


def possible(c):
    numbers = list(str(c))
    for number in numbers:
        if broken[int(number)]:
            return 0
    else:
        return len(numbers)

# 100번에서 n번까지 +, -만 눌러서 채널을 바꿨을 때.
ans = abs(n - 100)
# 숫자를 누른 다음 +, - 버튼을 눌러 채널을 바꿨을 때.
for c in range(0, 1000001):
    button_count = possible(c)
    if not button_count:
        continue
    ans = min(abs(c - n) + button_count, ans)

print(ans)
