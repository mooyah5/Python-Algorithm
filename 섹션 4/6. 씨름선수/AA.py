# 씨름선수 (그리디)
# 유사문제 - 백준의 '신입사원'

# 감독선수가 씨름선수 선발 공고를 냈다.
# N명의 지원자들을 다른 모든 지원자들과 1:1 비교하여, 키와 몸무게 중 적어도 하나는 큰 지원자만 선발한다.
# 반대로 A지원자보다 키와 몸무게 모두 큰 다른 지원자가 존재한다면 A 지원자는 탈락한다는 의미이다,

# 입력
# 첫째줄에 지원자 수 N이 주어지며, 이후로 N명의 키, 몸무게가 공백으로 구분되어 주어진다.

# 출력
# 선발 최대 인원을 출력하세용

# 1. 이중 for문
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# arr = sorted(arr, key=lambda x: (x[0], x[1]))
# cnt = 1
# for i in range(N - 1):
#     state = True
#     for j in range(i + 1, N):
#         if arr[i][1] < arr[j][1]:
#             state = False
#             break
#     if state:
#         cnt += 1
# print(cnt)

# 2. 더 간단히 (내림차순 후 최대 몸무게와 비교)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (-x[0], -x[1]))
cnt = 0
largest = -1
for a in arr:
    if a[1] > largest:
        largest = a[1]
        cnt += 1
print(cnt)
