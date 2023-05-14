# 최대점수 구하기 (DFS)

# 제한시간 M안에 N개의 숙제를 최대 성적으로 풀기
# 각 문제 별 점수, 걸리는 시간 주어진다

def DFS(i, score, time):
    global largest
    # 시간 초과 시 빠꾸
    if time > M:
        return
    # N개의 숫자 도달 시 최댓값과 비교 후 빠꾸
    if i == N:
        if largest < score:
            largest = score
        return
    DFS(i+1, score + arr[i][0], time + arr[i][1])  # 다음 숫자 추가하며 단계 진행
    DFS(i+1, score, time)                         # 다음 숫자 미포함하며 단계 진행
    return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
largest = -1    # 가장 높은 점수로 갱신될 정답
DFS(0, 0, 0)    # arr인덱스, 점수합, 시간합
print(largest)
