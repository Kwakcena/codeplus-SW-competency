def prev_permutation(nums):
    for i in reversed(range(len(nums) - 1)):
        if nums[i + 1] < nums[i]:
            break
    else:
        return -1

    j = next(j for j in reversed(range(i + 1, len(nums))) if nums[i] > nums[j])

    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])

    return nums


def print_answer(answer):
    for lottos in answer:
        for lotto in lottos:
            print(lotto)
        print()


def select_lotto():
    case = []
    selected = [1 if i < 6 else 0 for i in range(k)]

    while selected != -1:
        temp = []
        for index, value in enumerate(selected):
            if value == 1:
                temp.append(numbers[index + 1])
        case.append(str(temp)[1:-1].replace(', ', ' '))
        selected = prev_permutation(selected)

    return case

if __name__ == "__main__":
    answer = []
    while True:
        numbers = list(map(int, input().split()))
        k = numbers[0]

        if k == 0:
            break

        answer.append(select_lotto())
    print_answer(answer)
