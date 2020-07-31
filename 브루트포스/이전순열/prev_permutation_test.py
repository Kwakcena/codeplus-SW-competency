def test_next_permutation():
    assert next_permutation([5, 4, 3, 2, 1]) == -1
    assert next_permutation([7, 2, 3, 6, 5, 4, 1]) == "7 2 4 1 3 5 6"
    assert next_permutation([1, 2, 3, 4]) == "1 2 4 3"


def next_permutation(numbers):
    for i in reversed(range(len(numbers) - 1)):
        if numbers[i + 1] > numbers[i]:
            break
    else:
        return -1

    j = next(j for j in reversed(range(i+1, len(numbers))) if numbers[i] < numbers[j])

    numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i+1:] = reversed(numbers[i+1:])

    return str(numbers)[1:-1].replace(', ', ' ')


def test_prev_permutation():
    assert prev_permutation([1, 2, 3, 4]) == -1
    assert prev_permutation([5, 4, 3, 2, 1]) == "5 4 3 1 2"


def prev_permutation(numbers):
    for i in reversed(range(len(numbers) - 1)):
        if numbers[i + 1] < numbers[i]:
            break
    else:
        return -1

    j = next(j for j in reversed(range(i+1, len(numbers))) if numbers[i] > numbers[j])

    numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i+1:] = reversed(numbers[i+1:])

    return str(numbers)[1:-1].replace(', ', ' ')


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(prev_permutation((numbers)))