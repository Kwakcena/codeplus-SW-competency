from itertools import permutations


def get_permutations(array, n):
    return list(permutations(sorted(array), n))


def solution(n, list):
    permutations = get_permutations(list, n)
    find_tuple = tuple(list)
    for index, item in enumerate(permutations):
        if item == find_tuple:
            return str(permutations[index + 1])[1:-1].replace(',', '')
        else:
            return -1


if __name__ == "__main__":
    n = int(input())
    find = list(map(int, input().split()))
    print(solution(n, find))


def test_solution():
    assert solution(4, [1, 2, 3, 4]) == (1, 2, 4, 3)
    assert solution(5, [5, 4, 3, 2, 1]) == -1
