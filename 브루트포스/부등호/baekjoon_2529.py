from itertools import permutations

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k = int(input())
sign = input().split()

small = numbers[:k + 1]
big = list(reversed(numbers[-(k + 1):]))


def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] >= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


def check(permute):
    for i in range(len(sign)):
        if sign[i] == '<' and permute[i] > permute[i + 1]:
            return False
        if sign[i] == '>' and permute[i] < permute[i + 1]:
            return False
    return True


while True:
    if check(small):
        break
    if not next_permutation(small):
        break

while True:
    if check(big):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str, big)))
print(''.join(map(str, small)))
