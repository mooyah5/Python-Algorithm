# 랜선자르기 (결정 알고리즘, 이분탐색)

# 랜선의 개수 K
# 잘린 랜선 길이는 최소 N개 이상이어야 한다.
# K개의 랜선 길이가 주어지면, N개 이상으로 자를 수 있는 랜선 길이의 최대치를 출력하라.

# 1)
# def Count(mid):       # 해당 길이로 잘랐을 경우 만들어지는 랜선 개수
#     cnt = 0
#     for a in arr:
#         cnt += a//mid
#     return cnt


# K, N = map(int, input().split())
# arr = []
# for i in range(K):
#     arr.append(int(input()))

# s, e = 0, sum(arr)//N     # 이분탐색 위한 start, end 값
# res = 0
# while s <= e:
#     mid = (s+e)//2        # 중간 값 지정
#     if Count(mid) >= N:   # 그 중간값이 N개 이상이면
#         res = mid             # res는 그 중간값이며
#         s = mid + 1           # start는 mid+1 부터로 올려준다.
#     else:                 # 그 중간값으로 N개 이상의 랜선을 만들지 못하면
#         e = mid - 1           # end 값을 mid-1 까지로 내려준다.
# print(res)


# 2) 20230725 재도전
N, M = map(int, input().split())
arr = [int(input()) for i in range(N)]
arr.sort(reverse=True)
s = 1  # Error (Zero Division): start가 0이면 mid가 0이 될 수 있다.
e = sum(arr) // N
largest = -1
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for a in arr:
        cnt += a // mid
    if cnt >= M:
        largest = mid
        s = mid + 1
    elif cnt < M:
        e = mid - 1
print(largest)
