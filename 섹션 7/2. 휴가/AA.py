# 휴가 (SWEA 기출, DFS)

# 카운셀러 현수는 오늘로부터 N+1일째 날에 휴가 갈 거임
# 남은 N일 동안 최대한 많은 상담으로 휴가비 넉넉하게
# 회사에 하루 한 번 상담 예약 (서로 다른 사람)
# 각 상담은 상담기간(일) T, 대가(금액) P로 구성

def DFS(i, P):
    global largest
    if i == N:
        if largest < P:
            largest = P
        return
    if i + Ts[i] <= N:
        DFS(i+Ts[i], P+Ps[i])
    DFS(i+1, P)
    return


N = int(input())
Ts = []   # i+1일 상담의 상담기간(일수 T)
Ps = []   # i+1일 상담의 상담대가(금액 P)
for i in range(N):
    a, b = map(int, input().split())
    Ts.append(a)
    Ps.append(b)

largest = -1
DFS(0, 0)
print(largest)
