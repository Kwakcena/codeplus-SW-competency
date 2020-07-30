n = int(input())

def f(case):
    if case == 1:
        return 1
    if case == 2:
        return 2
    if case == 3:
        return 4
    return f(case - 1) + f(case - 2) + f(case - 3)

while n != 0:
    test_case = int(input())
    print(f(test_case))
    n -= 1