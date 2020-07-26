def GCD(n, m):
    return n if m == 0 else GCD(m, n%m)

def LCM(gcd, n, m):
    return (n * m) // gcd

n, m = map(int, input().split())
g = GCD(n, m)
l = LCM(g, n, m)

print(f"{g}\n{l}")

def test_GCD():
    assert GCD(24, 18) == 6

def test_LCM():
    assert LCM(6, 24, 18) == 72


