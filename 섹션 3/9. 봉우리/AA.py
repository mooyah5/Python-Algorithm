# 봉우리

# N*N 지도정보가 격자판에 주어지며, 각 격자는 그 지역의 높이
# 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역이다.
# 봉우리 지역의 개수를 출력하세여

# 1)

# 1. 입력 받고, 상하좌우에 0 배열 한줄씩 추가하기
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arr.insert(0, [0]*N)  # 상
arr.append([0]*N)     # 하
for a in arr:
    a.insert(0, 0)    # 좌
    a.append(0)       # 우

# 2. 상하좌우에 있는 값보다 작은 게 하나라도 있으면 continue, 아니면 cnt 추가
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] <= arr[i][j-1] or arr[i][j] <= arr[i-1][j] or arr[i][j] <= arr[i+1][j] or arr[i][j] <= arr[i][j+1]:
            continue
        else:
            cnt += 1
print(cnt)


# 2)


# 1. 상, 우, 하, 좌 방향 지정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 2. 입력 받고, 상하좌우에 0 배열 한줄씩 추가하기
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arr.insert(0, [0]*N)
arr.append([0]*N)
for a in arr:
    a.insert(0, 0)
    a.append(0)

# 3. 각 방향보다 작은 게 있으면 넘어가고, 아니면 개수 추가
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if any(arr[i][j] <= arr[i+dx[k]][j+dy[k]] for k in range(4)):
            continue
        else:
            cnt += 1
print(cnt)
