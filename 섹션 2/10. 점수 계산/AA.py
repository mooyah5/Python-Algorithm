# 점수 계산

# OX문제 시험에서 연속으로 맞추면 가산점 준다.
# 연속 k번째의 답은 k점으로 계산 (틀리면 0)
import sys
# sys.stdin = open('in2.txt', 'rt')
N = int(input())    # 문제 개수
arr = list(map(int, input().split()))
# # print(arr)
# res = 0

# stack = [arr[0]]
# for i in range(1, len(arr)):
#     if arr[i] == 0:
#         stack.append(0)
#         continue
#     else:  # 1이면
#         if stack[-1] > 0:  # 스택의 마지막 값이 0보다 크면
#             stack.append(stack[-1] + 1)  # 스택에 마지막값+1을 추가
#             res += stack[-1]        # res에도 마지막값+1을 추가
#         else:   # 1인데 스택의 마지막값이 0이면
#             stack.append(1)  # 스택의 마지막값에 1을 추가
#             res += 1
# print(res)

res = 0
pre = 0
for i in range(0, N):
    if arr[i] == 0:
        pre = 0
        continue
    else:
        if pre:
            res += pre + 1
        else:
            res += 1
    pre += 1
print(res)
