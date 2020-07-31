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


if __name__ == "__main__":
    min = 1000001
    n = int(input())
    nums = [num for num in range(n)]
    board = [list(map(int, input().split())) for _ in range(n)]

    while nums != -1:
        sum = 0
        ok = True
        for i in range(len(nums) - 1):
            if not board[nums[i]][nums[i + 1]]:
                ok = False
            else:
                sum += board[nums[i]][nums[i + 1]]
        if ok and board[nums[len(nums) - 1]][nums[0]] != 0:
            sum += board[nums[len(nums) - 1]][nums[0]]
            if min > sum:
                min = sum
        nums = next_permutation(nums)

    print(min)
