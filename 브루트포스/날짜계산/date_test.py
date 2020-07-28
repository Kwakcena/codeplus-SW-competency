e, s, m = map(int, input().split())
year = 0

e -= 1
s -= 1
m -= 1
while True:
    if year % 15 == e and year % 28 == s and year % 19 == m:
        print(year + 1)
        break
    year += 1



