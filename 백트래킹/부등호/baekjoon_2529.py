def good(prev, curt, op):
    if op == '<' and prev > curt:
        return False
    if op == '>' and prev < curt:
        return False
    return True


def go(index, num):
    if index == k + 1:
        ans.append(num)
        return

    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(int(num[index - 1]), i, operators[index - 1]):
            check[i] = True
            go(index + 1, num + str(i))
            check[i] = False


k = int(input())
operators = input().split()
check = [False] * 10
ans = []

go(0, '')

print(ans[len(ans) - 1])
print(ans[0])