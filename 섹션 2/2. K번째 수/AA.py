import sys
T = int(input())
for tc in range(1, T+1):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = sorted(arr[s-1:e])[k-1]
    # print(arr)
    print("#%d %d" % (tc, ans))
