# 입력: 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
import sys


def selection_sort(_nums):
    for i in range(0, N):
        min_index = i
        for j in range(i, N):
            if nums[min_index] > nums[j]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]


N = int(sys.stdin.readline().rstrip())
nums = [0 for i in range(0, N)]

for i in range(0, N):
    nums[i] = int(sys.stdin.readline().rstrip())

selection_sort(nums)
for i in range(0, N):
    print(nums[i])
