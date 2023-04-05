# 두 리스트 합치기

# 오름차순 정렬된 두 리스트가 주어진다.
# 두 리스트를 합쳐 오름차순으로 정렬하여 출력

# 1) +로 합치고 sort함수 이용하기
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))
# C = A + B
# print(*sorted(C))

# 2)
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
p1 = p2 = 0
C = list()
while p1 < N and p2 < M:    # p1, p2 모두 범위를 벗어나지 않도록
    if A[p1] <= B[p2]:      # p1이 p2보다 작거나 같으면
        C.append(A[p1])     # C에 A[p1]을 추가하고 p1 1 증가
        p1 += 1
    else:
        C.append(B[p2])     # p2가 작으면
        p2 += 1             # C에 B[p2]을 추가하고 p2 증가

    if p1 >= N:             # p1이 끝에 도달하면
        C += B[p2:]         # C에 B 나머지를 이어붙이고 끝내기
        break
    elif p2 >= M:           # p2가 끝에 도달하면
        C += A[p1:]         # C에 A 나머지를 이어붙이고 끝내기
        break
print(*C)
