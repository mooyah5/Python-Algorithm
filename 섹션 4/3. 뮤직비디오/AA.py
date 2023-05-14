# 뮤직비디오(결정알고리즘)

#
def Count(capacity):
    cnt = 1
    tot = 0
    for a in arr:
        if tot + a > capacity:
            cnt += 1
            tot = a
        else:
            tot += a
    return cnt


N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 1, sum(arr)
res = 0
while s <= e:
    mid = (s+e)//2
    if Count(mid) <= M:
        res = mid
        e = mid - 1
    else:
        s = mid + 1
print(res)
