K, N = map(int, input().split())  # 랜선개수, 필요 랜선 개수
arr = [int(input()) for _ in range(K)]
arr.sort(reverse=True)  # 내림차순 정렬
s, e = 1, sum(arr) // K  # 시작, 끝점 설정 (e는 모든 수의 합을 개수만큼 나눈 것보다 클 수 없음.)
largest = -1  # 비교할 최대 길이 ( 답 )
while s <= e:  # s가 e보다 커지지 않는 선에서 반복
    mid = (s + e) // 2  # s와 e 사이 중간값으로 계속 비교한다.
    cnt = 0
    for a in arr:
        cnt += a // mid
    if cnt >= N:  # 개수가 N 이상이면 largest를 바꿔주고, 시작점을 중간점 위로 재설정한다.
        largest = mid
        s = mid + 1
    else:  # 개수가 N 미만이면 끝점을 중간점 아래로 재설정한다.
        e = mid - 1
print(largest)
