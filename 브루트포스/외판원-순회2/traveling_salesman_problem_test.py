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


def get_permutations(nums):
    permutations = []
    while nums != -1:
        permutations.append(nums[:])
        nums = next_permutation(nums)
    return permutations


if __name__ == "__main__":
    min = 1000001
    n = int(input())
    nums = [num for num in range(n)]
    board = [list(map(int, input().split())) for _ in range(n)]

    routes = get_permutations(nums)
    for route in routes:
        total = 0
        for i in range(len(route)):
            start = route[i]
            if i == len(route) - 1:
                end = route[0]
            else:
                end = route[i + 1]
            total += board[start][end]
        if total < min:
            min = total
        print(route, total)

    print(min)
