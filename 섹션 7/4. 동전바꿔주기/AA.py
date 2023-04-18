# 동전바꿔주기 (못풀음)

# 현급출납기에 K가지 동전
# T원의 지폐를 동전으로 바꿔주자
# 다양한 동전 교환 방법 가지 수 x 구하기

# x < 2**31

def DFS(i, tot):
    global N, T, ans
    if tot > T:
        return
    if i == N:
        if tot == T:
            ans += 1
            print('1', i, tot, T)
        return
    if tot == T:
        ans += 1
        print('2', i, tot, T)
        return
    DFS(i+1, tot + P[i])
    DFS(i+1, tot)


T = int(input())    # 거슬러 줄 지폐
K = int(input())    # 동전종류 수
P = []    # 동전금액
for k in range(K):
    p, n = map(int, input().split())
    for i in range(n):
        P.append(p)
print(P)
ans = 0
N = len(P)

DFS(0, 0)
print(ans)
