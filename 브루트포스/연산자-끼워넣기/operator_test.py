def next_permutation(nums):
    for i in reversed(range(len(nums) - 1)):
        if nums[i + 1] > nums[i]:
            break
    else:
        return -1

    j = next(j for j in reversed(range(i + 1, len(nums))) if nums[i] < nums[j])

    nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])

    return nums


def get_operator(nums):
    operator = []
    for i, x in enumerate(nums):
        for j in range(x):
            operator.append(i)

    return operator


def solution(n, nums, operator_nums):
    operators = sorted(get_operator(operator_nums))
    max_value, min_value = -2000000000, 2000000000

    while True:
        temp = calculate(n, nums, operators)
        if max_value < temp:
            max_value = temp
        if min_value > temp:
            min_value = temp

        operators = next_permutation(operators)
        if operators == -1:
            break

    return [max_value, min_value]


def calculate(n, nums, operators):
    answer = nums[0]
    for i in range(1, n):
        if operators[i - 1] == 0:
            answer += nums[i]
        elif operators[i - 1] == 1:
            answer -= nums[i]
        elif operators[i - 1] == 2:
            answer *= nums[i]
        else:
            if answer < 0:
                answer = -( -answer // nums[i])
            else:
                answer //= nums[i]
    return answer


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    nums_operator = list(map(int, input().strip().split()))

    answer = solution(n, nums, nums_operator)
    print(answer[0])
    print(answer[1])


def test_solution():
    assert solution(2, [5, 6], [0, 0, 1, 0]) == [30, 30]
    assert solution(3, [3, 4, 5], [1, 0, 1, 0]) == [35, 17]
    assert solution(6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1]) == [54, -24]
    assert solution(3, [10, 11, 3], [0, 1, 0, 1]) == [0, -3]
    assert solution(2, [-7, 6], [0, 0, 0, 1]) == [-1, -1]
    assert solution(5, [100, 100, 1, 100, 100], [1, 1, 1, 1]) == [19900, -9800]
    assert solution(5, [100, 100, 100, 100, 10], [0, 0, 4, 0]) == [1000000000,
                                                                   1000000000]
    assert solution(2, [1, 2], [0, 1, 0, 0]) == [-1, -1]
    assert solution(3, [1, 2, 3], [1, 1, 0, 0]) == [2, 0]


def test_calculate():
    assert calculate(2, [5, 6], [2]) == 30
    assert calculate(3, [3, 4, 5], [0, 2]) == 35
    assert calculate(3, [3, 4, 5], [2, 0]) == 17
    assert calculate(6, [1, 2, 3, 4, 5, 6], [1, 3, 0, 0, 2]) == 54
    assert calculate(6, [1, 2, 3, 4, 5, 6], [0, 0, 3, 1, 2]) == -24


def test_get_operator():
    assert get_operator([0, 0, 1, 0]) == [2]
    assert get_operator([1, 0, 1, 0]) == [0, 2]
    assert get_operator([2, 1, 1, 1]) == [0, 0, 1, 2, 3]


def test_next_permutation():
    assert next_permutation([1, 2, 3, 4, 5]) == [1, 2, 3, 5, 4]
    assert next_permutation([5, 4, 3, 2, 1]) == -1
    assert next_permutation([0, 0, 1, 0]) == [0, 1, 0, 0]
