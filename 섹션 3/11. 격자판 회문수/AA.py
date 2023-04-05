arr = [list(map(int, input().split())) for i in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        a = []
        b = []
        for k in range(5):
            a.append(arr[i][j+k])
            b.append(arr[j+k][i])
        if a == a[::-1]:
            cnt += 1
        if b == b[::-1]:
            cnt += 1
print(cnt)
