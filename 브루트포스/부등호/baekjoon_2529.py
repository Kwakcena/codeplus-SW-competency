from itertools import permutations

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k = int(input())
sign = input().split()

small = list(permutations(numbers[:k + 1], k + 1))
big = list(permutations(reversed(numbers[-(k + 1):]), k + 1))


def check(permute):
    for i in range(len(sign)):
        if sign[i] == '<' and permute[i] > permute[i + 1]:
            return False
        if sign[i] == '>' and permute[i] < permute[i + 1]:
            return False
    return True


small_ans = next(s for s in small if check(s))
big_ans = next(b for b in big if check(b))

print(''.join(map(str, small_ans)))
print(''.join(map(str, big_ans)))
