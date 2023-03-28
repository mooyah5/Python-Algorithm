# 주사위 게임

# 주사위 3개를 던진다.

# 규칙 1. 같은눈 3개면, 만원 + 같은눈*천원
# 규칙 2. 같은눈 2개면, 천원 + 같은눈*백원
# 규칙 3. 모누 다른눈,       가장큰눈*백원

# 참여자 중 가장 많은 상금을 받은 사람의 상금을 출력

# # 내가 푼 답
# import sys
# sys.stdin = open('in4.txt', 'rt')
# T = int(input())    # 참여자 수
# res = []
# for tc in range(T):
#     arr = list(map(int, input().split()))
#     if arr[0] == arr[1] or arr[0] == arr[2]:
#         if arr[1] == arr[2]:  # 모두 같은 눈
#             res.append(arr[0]*1000+10000)
#         else:   # 첫번째 인덱스와 2개만 겹치면
#             res.append(arr[0]*100+1000)
#     else:
#         if arr[1] == arr[2]:  # 2개만 겹치면
#             res.append(arr[0]*100+1000)
#         else:  # 아무것도 안 겹치면
#             res.append(max(arr)*100)
# print(max(res))


# 해설
import sys
# sys.stdin = open('in1.txt', 'rt')
T = int(input())    # 참여자 수
res = 0
for tc in range(T):
    arr = sorted(list(map(int, input().split())))  # 오름차순이므로 가장 마지막 눈이 크다.
    a, b, c = map(int, arr)
    if a == b and b == c:     # 세 눈이 모두 같다
        money = 10000+a*1000
    elif a == b or a == c:    # 두 눈이 같다
        money = 1000+a*100
    elif b == c:              # 두 눈이 같다
        money = 1000+b*100
    else:                     # 세 눈이 모두 다르다
        money = c*100
    if money > res:           # 최댓값보다 크면 최댓값 갱신
        res = money
print(res)
