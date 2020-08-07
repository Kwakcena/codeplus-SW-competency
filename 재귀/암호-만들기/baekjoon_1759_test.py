L, C = map(int, input().split())
alpabet = sorted(list(input().split()))


def check(string):
    ja, mo = 0, 0
    for ch in list(string):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def solution(index, ans):
    # 정답을 출력하는 조건
    if len(ans) == L:
        if check(ans):
            print(ans)
        return

    # 불가능 조건
    if index >= C:
        return

    # 다음 단계
    solution(index+1, ans + alpabet[index])
    solution(index+1, ans)


solution(0, '')
