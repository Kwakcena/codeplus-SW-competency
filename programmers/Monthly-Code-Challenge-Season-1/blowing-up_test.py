def test_solution():
    assert solution([9, -1, -5]) == 3
    assert solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]) == 6


def get_min_balloon(arr):
    if len(arr) == 0:
        return 10**9 + 1
    return min(arr)


def solution(a):
    ans = 0
    for i in range(len(a)):
        left_min = get_min_balloon(a[:i])
        right_min = get_min_balloon(a[i + 1:])
        if a[i] >= left_min and a[i] >= right_min:
            continue
        ans += 1
    return ans