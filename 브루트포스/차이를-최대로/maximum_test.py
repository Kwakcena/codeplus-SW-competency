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


def get_maximum(nums):
    sum = 0
    for i in range(len(nums) - 1):
        sum += abs(nums[i] - nums[i + 1])
    return sum


if __name__ == "__main__":
    n = int(input())
    nums = sorted(list(map(int, input().split())))

    max = 0
    while nums != -1:
        temp = get_maximum(nums)
        if max < temp:
            max = temp
        nums = next_permutation(nums)

    print(max)
