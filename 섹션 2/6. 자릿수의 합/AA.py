# 자릿수의 합

# N개의 자연수가 입력된다.
# 각 자연수 자릿수의 합을 구하고
# 그 합이 최대인 자연수를 출력하라.
import sys
# sys.stdin = open('in2.txt', 'rt')
N = int(input())  # 자연수의 개수
arr = list(map(int, input().split()))

# 내가 푼 답1
# def sum_all(arr):               # 리스트 요소 자릿수 합 중 최대값의 인덱스를 반환
#     arr = map(str, arr)
#     res = []
#     for a in arr:
#         tmp = 0
#         for i in range(len(a)):
#             tmp += int(a[i])
#         res.append(tmp)
#     return res.index(max(res))
# print(arr[sum_all(arr)])

# 내가푼답2
# def digit_sum(a):
#     a = str(a)
#     res = 0
#     for n in a:
#         res += int(n)
#     return res
# maxtot = -2714000000
# maxN = -2714000000
# for a in arr:
#     tot = digit_sum(a)
#     # print(tot)
#     if maxtot < tot:
#         maxtot = tot
#         maxN = a
# print(maxN)


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum


maxN = -2174000000  # 2**31 (c++등이 최대 저장 가능한 수) 실제로는 2147483647
for x in arr:
    tot = digit_sum(x)
    if tot > maxN:
        maxN = tot
        res = x
print(res)
