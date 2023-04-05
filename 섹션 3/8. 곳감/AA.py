# 곳감 (모래시계)

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
M = int(input())    # 회전 수
for m in range(M):
    l, d, f = map(int, input().split())  # line, direction, frequency
    if d == 0:  # 왼쪽
        for i in range(f):
            arr[l-1].append(arr[l-1].pop(0))
    else:
        for i in range(f):
            arr[l-1].insert(0, arr[l-1].pop(-1))
s, e = 0, N-1
cnt = 0
for i in range(N):
    for j in range(s, e+1):
        cnt += arr[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(cnt)
