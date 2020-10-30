def prev_permutaion(a):
    i = len(a) - 1
    while i >= 0 and a[i - 1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[i - 1] <= a[j]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i <= j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


n = int(input())
strs = [input() for _ in range(n)]

alpha = {}
unique_char = list(set(''.join(strs)))
numbers = [9 - i for i in range(len(unique_char))]

ans = 0
while True:
    for c, n in zip(unique_char, numbers):
        alpha[c] = n

    res = 0
    for str in strs:
        m = len(str) - 1
        for c in list(str):
            res += alpha[c] * (10 ** m)
            m -= 1
    ans = max(ans, res)

    if not prev_permutaion(numbers):
        break

print(ans)
