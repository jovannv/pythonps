# N×N크기의 행렬로 표현되는 종이가 있다.
# 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다.
# 우리는 이 행렬을 적절한 크기로 자르려고 하는데,
# 이때 다음의 규칙에 따라 자르려고 한다.
#
# 1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# 2. (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고,
# 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수,
# 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# 입력: 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다.
# 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

# 출력: 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를,
# 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

import sys


def get_paper_cnt(matrix, y, x, width):
    # 제일 작은 종이 조각일 때
    if width == 1:
        if matrix[y][x] == -1:
            return 1, 0, 0, 1, 0, 0
        elif matrix[y][x] == 0:
            return 0, 1, 0, 0, 1, 0
        elif matrix[y][x] == 1:
            return 0, 0, 1, 0, 0, 1

    cnt = [0, 0, 0, 0, 0, 0]

    max_total = width * width
    width = int(width / 3)
    height = width

    for i in range(3):
        for j in range(3):
            temp_cnt = get_paper_cnt(matrix, y + height * i, x + width * j, width)
            for k in range(6):
                cnt[k] = cnt[k] + temp_cnt[k]

    if cnt[0] == max_total:
        cnt[3] = 1

    if cnt[1] == max_total:
        cnt[4] = 1

    if cnt[2] == max_total:
        cnt[5] = 1

    return cnt


N = int(sys.stdin.readline().rstrip())
case = [list(map(int, sys.stdin.readline().rstrip().split())) for y in range(N)]

paper_cnt = get_paper_cnt(case, 0, 0, N)
print(paper_cnt[3])    # -1로만 채워진 종이의 개수
print(paper_cnt[4])    # 0으로만 채워진 종이의 개수
print(paper_cnt[5])    # 1로만 채워진 종이의 개수
