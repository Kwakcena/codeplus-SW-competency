def test_eratos():
    assert eratos(19) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert eratos(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                           43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def eratos(m):
    check = [False] * (m + 1)
    prime_numbers = []
    for i in range(2, m + 1):
        if not check[i]:
            prime_numbers.append(i)
            for j in range(i + i, m + 1, i):
                check[j] = True

    return [prime_numbers, check]


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    [prime_numbers, check] = eratos(max(numbers))

    count = 0
    for number in numbers:
        if number != 1 and not check[number]:
            count += 1
    print(count)
