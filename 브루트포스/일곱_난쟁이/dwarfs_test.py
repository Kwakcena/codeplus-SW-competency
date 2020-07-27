# 1. 9명 중 2명을 구한다.
# 2. 나머지 7명의 합을 구한다.
# 3. 합이 100이면 7명을 오름차순 정렬하여 출력한다.

def test_solution():
    assert solution([20, 7, 23, 19, 10, 15, 25, 8, 13]) == [7, 8, 10, 13, 19,
                                                            20,
                                                            23]


def solution(dwarfs):
    heights = sum(dwarfs)
    for i in dwarfs:
        for j in dwarfs:
            if i == j:
                continue
            if heights - (i + j) == 100:
                dwarfs.remove(i)
                dwarfs.remove(j)
                return sorted(dwarfs)


if __name__ == "__main__":
    dwarfs = [int(input()) for _ in range(9)]
    for dwarf in solution(dwarfs):
        print(dwarf)
