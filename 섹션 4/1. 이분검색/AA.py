# 이분검색

# 임의의 N개의 숫자가 입력으로 주어진다.
# N개의 수를 오름차 정렬한 후, 그 중 한 수인 M이 주어지면
# 이분검색으로 몇 번째에 있는지 구해보렴
# 1024개면, 1024-512-256... 이렇게 줄어들어서 log n 번이다 이말이야

# 1) 재귀
# def binary_search(M, arr, s, e):
#     mid = (s+e) // 2
#     if arr[mid] == M:
#         return mid
#     elif arr[mid] > M:
#         e = mid-1
#     else:
#         s = mid+1
#     return binary_search(M, arr, s, e)


# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# ans = 0
# print(binary_search(M, arr, 0, N-1) + 1)  # arr, start, end

# 2) while
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# s, e = 0, N-1
# while (s <= e):
#     mid = (s+e) // 2
#     if arr[mid] == M:
#         print(mid+1)
#         break
#     elif arr[mid] > M:
#         e = mid - 1
#     else:
#         s = mid + 1


# 3) 0725 재도전
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
i = N // 2
while 0 <= i < N:
    if arr[i] == M:
        print(i + 1)
        break
    elif arr[i] < M:
        i += 1
    else:
        i -= 1
