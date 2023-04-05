# 수들의 합

# 투포인터 활용

# N개의 수로 된 수열이 있을 때,
# i번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하라

# 1)
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# s, e = 0, 1
# cnt = 0
# while s < e:
#     if sum(A[s:e+1]) == M:
#         print(A[s:e+1])
#         cnt += 1

#     if sum(A[s:e+1]) >= M:
#         s += 1
#     else:
#         e += 1
# print(cnt)

# 2)
M = map(int, input().split())
A = list(map(int, input().split()))
s, e = 0, 1
cnt = 0
while s < e:
    if sum(A[s:e+1]) == M:
        print(A[s:e+1])
        cnt += 1

    if sum(A[s:e+1]) >= M:
        s += 1
    else:
        e += 1
print(cnt)
