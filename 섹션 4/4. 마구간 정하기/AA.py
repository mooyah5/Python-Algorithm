# 마구간 정하기

# N개의 숫자가 주어지면, 오름차순 정렬 후
# M을 이분검색으로 찾아 몇번째에 있는지 구하
def Count(leng):
    cnt = 1
    end = arr[0]
    for i in range(1, n):
        if arr[i]
    return


N, C = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr.sort()
s, e = 0, N-1
mid = N//2
res = 0
while s <= e:
    mid = (s+e)//2
    if Count[mid] >= C:
        res = mid
        e = mid - 1
    else:
        s = mid + 1
