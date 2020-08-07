def solution(sum, goal):
    if sum > goal:
        return 0
    if sum == goal:
        return 1

    ans = 0
    for i in range(1, 4):
        ans += solution(sum+i, goal)
    return ans

if __name__=="__main__":
    n = int(input())
    for i in range(n):
        case = int(input())
        print(solution(0, case))


def test_solution():
    assert solution(0, 4) == 7
    assert solution(0, 7) == 44
    assert solution(0, 10) == 274