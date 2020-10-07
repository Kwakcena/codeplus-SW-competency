from itertools import combinations

def test_solution():
    assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
    assert solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12]


def solution(numbers):
    return list(
        sorted(set([sum(num) for num in list(combinations(numbers, 2))]))
    )