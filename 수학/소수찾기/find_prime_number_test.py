def test_eratos():
    assert eratos(19) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert eratos(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                           43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def test_find_prime_number():
    assert find_prime_number(2) == True
    assert find_prime_number(3) == True
    assert find_prime_number(4) == False
    assert find_prime_number(100) == False
    assert find_prime_number(19) == True


def find_prime_number(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True


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
