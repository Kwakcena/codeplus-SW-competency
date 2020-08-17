import sys

n = 20
m = int(sys.stdin.readline())
s = 0

for _ in range(m):
    operator, *num = sys.stdin.readline().split()
    if len(num) > 0:
        x = int(num[0]) - 1
    if operator == "add":
        s = (s | (1 << x))
    elif operator == "remove":
        s = (s & ~(1 << x))
    elif operator == "check":
        result = (s & (1 << x))
        if result > 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif operator == "toggle":
        s = (s ^ (1 << x))
    elif operator == "all":
        s = (1 << n) - 1
    elif operator == "empty":
        s = 0
