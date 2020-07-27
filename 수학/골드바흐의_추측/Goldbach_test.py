def prime_number_list(m):
    check = [False] * (m + 1)
    prime_numbers = []
    for i in range(2, m + 1):
        if not check[i]:
            # 홀수 소수만 구한다.
            if i % 2 == 1:
                prime_numbers.append(i)
            for j in range(i + i, m + 1, i):
                check[j] = True

    return [prime_numbers, check]


def get_glodbach(n, primes, check):
    for prime in primes:
        if not check[n - prime]:
            return f"{n} = {prime} + {n - prime}"
        if n < prime:
            break
    return "Goldbach's conjecture is wrong."


if __name__ == "__main__":
    n = 0
    [primes, check] = prime_number_list(1000000)
    while True:
        n = int(input())
        if not n:
            break
        print(get_glodbach(n, primes, check))
