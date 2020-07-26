def GCD(n, m):
    return n if m == 0 else GCD(m, n % m)


def LCM(gcd, n, m):
    return (n * m) // gcd


def solution(n, m):
    return LCM(GCD(n, m), n, m)


if __name__ == "__main__":
    repeat = int(input())
    for i in range(repeat):
        n, m = map(int, input().split())
        print(solution(n, m))


def test_solution():
    assert solution(1, 45000) == 45000
    assert solution(6, 10) == 30
    assert solution(13, 17) == 221
