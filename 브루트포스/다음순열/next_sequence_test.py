def test_next_permutation():
    assert next_permutation([7, 2, 3, 6, 5, 4, 1]) == "7 2 4 1 3 5 6"
    assert next_permutation([1, 2, 3, 4]) == "1 2 4 3"
    assert next_permutation([5, 4, 3, 2, 1]) == -1


def next_permutation(numbers):
    # numbers[i] < numbers[i+1]을 만족하는 가장 큰 index i를 찾는다.
    for i in reversed(range(len(numbers) - 1)):
        if numbers[i] < numbers[i + 1]:
            break
    else:
        return -1

    # i보다 크고 numbers[i] < numbers[j]를 만족하는 가장 큰 index j를 찾는다.
    j = next(j for j in reversed(range(i + 1, len(numbers))) if
         numbers[i] < numbers[j])

    # i와 j index의 값을 바꾼다.
    numbers[i], numbers[j] = numbers[j], numbers[i]

    # i+1 자리부터 끝까지의 값을 뒤집어 넣는다.
    numbers[i + 1:] = reversed(numbers[i + 1:])

    return str(numbers)[1:-1].replace(', ', ' ')


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(next_permutation(numbers))