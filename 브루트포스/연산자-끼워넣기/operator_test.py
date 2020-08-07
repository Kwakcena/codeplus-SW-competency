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


def test_next_permutation():
    assert next_permutation([1, 2, 3, 4, 5]) == [1, 2, 3, 5, 4]
    assert next_permutation([5, 4, 3, 2, 1]) == -1
    assert next_permutation([0, 0, 1, 0]) == [0, 1, 0, 0]
