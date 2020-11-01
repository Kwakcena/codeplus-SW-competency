from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

player = [i for i in range(1, n + 1)]
min_value = float('inf')

for combination in list(combinations(player, n // 2)):
    start_team = combination
    link_team = tuple(i for i in player if i not in start_team)

    start_ans, link_ans = 0, 0
    for start_index, link_index in zip(list(combinations(start_team, 2)),
                                       list(combinations(link_team, 2))):
        start_ans += (s[start_index[0] - 1][start_index[1] - 1] +
                      s[start_index[1] - 1][start_index[0] - 1])
        link_ans += (s[link_index[0] - 1][link_index[1] - 1] +
                     s[link_index[1] - 1][link_index[0] - 1])

    comp = abs(start_ans - link_ans)
    if min_value > comp:
        min_value = comp

print(min_value)
