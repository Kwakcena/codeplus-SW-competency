def test_solution():
    assert solution([9, -1, -5]) == 3
    assert solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]) == 6


def solution(a):
    left_index = 0
    right_index = len(a) - 1

    min_count = [0] * len(a)

    left_min_value = a[left_index]
    for i in range(1, len(a)):
        if left_min_value > a[i]:
            left_min_value = a[i]
            continue
        min_count[i] += 1

    right_min_value = a[right_index]
    for j in range(len(a) - 2, -1, -1):
        if right_min_value > a[j]:
            right_min_value = a[j]
            continue
        min_count[j] += 1

    return (len(list(filter(lambda x: x != 2, min_count))))
