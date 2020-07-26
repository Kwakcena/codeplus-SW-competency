from itertools import combinations

def GCD(n, m):
    return n if m == 0 else GCD(m, n%m)

if __name__=="__main__":
    repeat = int(input())
    for i in range(repeat):
        values = list(map(int, input().split()))
        sum = 0
        for n, m in list(combinations(values[1:], 2)):
            sum += GCD(n, m)
        print(sum)



def test_GCD():
    assert GCD(10, 20) == 10
    assert GCD(10, 30) == 10
    assert GCD(10, 40) == 10
    assert GCD(20, 30) == 10
    assert GCD(20, 40) == 20
    assert GCD(30, 40) == 10
