def go(index, numbers, k, ans):
    if len(ans) == 6:
        print(str(ans)[1:-1].replace(',', ''))
        return

    if index >= k:
        return

    ans.append(numbers[index])
    go(index + 1, numbers, k, ans)
    ans.pop()
    go(index + 1, numbers, k, ans)

if __name__=="__main__":
    k = -1
    while k != 0:
        test_case = list(map(int, input().split()))
        k = test_case[0]

        go(0, test_case[1:], k, [])
        print()