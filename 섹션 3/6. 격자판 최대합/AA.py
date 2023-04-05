# 격자판 최대합

# N*N 격자판에 숫자가 적혀있다.
# 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합 출력

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
ans = []

arr2 = []
b = 0
for i in range(N):
    a = []
    for j in range(N):
        a.append(arr[j][i])
        if i == j:
            b += arr[i][j]
    arr2.append(a)
ans.append(b)

for i in range(N):
    ans.append(sum(arr[i]))
    ans.append(sum(arr2[i]))
    c = 0
    if N-i-1 == 0:
        c += arr[i][N-i-1]
ans.append(c)


# print(ans)
print(max(ans))
