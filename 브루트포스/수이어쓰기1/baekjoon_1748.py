n = int(input())

ans = 0
unit = 10 ** (len(str(n)) - 1)
length = len(str(n))

while n:
    count = n - unit + 1
    unit //= 10
    ans += length * count

    n -= count
    length -= 1

print(ans)

