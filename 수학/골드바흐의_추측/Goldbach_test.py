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


if __name__ == "__main__":
    n = 0
    while True:
        n = int(input())
        [primes, check] = prime_number_list(n)
        for prime in primes:
            if not check[n - prime]:
                print(f"{n} = {prime} + {n - prime}")
                break
        if not n:
            break
