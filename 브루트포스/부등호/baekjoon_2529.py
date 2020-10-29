from itertools import permutations

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k = int(input())
sign = input().split()

answers = []
permutations_list = list(permutations(numbers, k + 1))

for permute in permutations_list:
    ok = False
    for i in range(len(permute) - 1):
        if sign[i] == '<':
            if permute[i] < permute[i + 1]:
                ok = True
            else:
                ok = False
                break
        if sign[i] == '>':
            if permute[i] > permute[i + 1]:
                ok = True
            else:
                ok = False
                break
    if ok:
        answers.append(str(permute)[1:-1].replace(', ', ''))

print(answers[len(answers) - 1])
print(answers[0])

