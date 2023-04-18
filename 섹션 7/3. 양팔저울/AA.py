# 한 번 더 풀어주라
# 양팔저울 (DFS)

# 무게가 서로 다른 K개의 추와 빈그릇 (그릇 무게 0)
# 양팔저울을 1회 사용하여 원하는 물 무게를 그릇에 담겠으
# 모든 추 무게의 합 S
# 양팔저울 1회 사용해서 1, 2, 3, ..., S 사이 측정 불가능한 무게 개수

def DFS(i, tot):
    global ans
    if i == K:
        if 0 < tot <= S:
            ans.add(tot)
        return
    DFS(i+1, tot+arr[i])
    DFS(i+1, tot)
    DFS(i+1, tot-arr[i])
    return


K = int(input())
arr = list(map(int, input().split()))
S = sum(arr)
ans = set()
DFS(0, 0)    # arr인덱스, 합
print(S-len(ans))
