import sys
from collections import Counter
from functools import reduce

N = int(sys.stdin.readline())
field = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 둘의 차이점?
# visited = [[0] * N] * N
visited = [[0 for _ in range(N)] for _ in range(N)]
address_number = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, number):
    visited[y][x] = number
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if N > new_x >= 0 and N > new_y >= 0:
            if field[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                dfs(new_y, new_x, number)

for y in range(N):
    for x in range(N):
        if field[y][x] == 1 and visited[y][x] == 0:
            address_number += 1
            dfs(y, x, address_number)

print(address_number)
# visited 2차원 리스트를 1차원 리스트로 만들어 준다.
ans = reduce(lambda x, y: x + y, visited)
# ans 1차원 배열에 있는 값 중 0보다 큰 값만 남겨놓는다.
ans = [x for x in ans if x > 0]
# Counter로 ans 리스트에 있는 숫자들을 카운트 하여 딕셔너리로 반환하고,
# 해당 딕셔너리의 값만 모아서 list로 만들어 오름차순으로 정렬한다.
ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str, ans)))