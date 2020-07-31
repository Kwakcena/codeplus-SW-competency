def next_permutation(nums):
    for i in reversed(range(len(nums) - 1)):
        if nums[i+1] > nums[i]:
            break
    else:
        return -1

    j = next(j for j in reversed(range(i+1, len(nums))) if nums[i] < nums[j])

    nums[i], nums[j] = nums[j], nums[i]

    nums[i+1:] = reversed(nums[i+1:])

    return nums


if __name__ == "__main__":
    n = int(input())
    nums = [num for num in range(1, n+1)]

    while nums != -1:
        print(str(nums)[1:-1].replace(', ', ' '))
        nums = next_permutation(nums)