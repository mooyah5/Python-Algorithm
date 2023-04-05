# 회문 문자열 검사

# N개의 문자열 입력받아 회문문자열(앞으로나뒤로나같으면)이면 YES, 아니면 NO 출력
import sys
# sys.stdin = open('in1.txt', 'rt')
N = int(input())    # 문자열 개수
for n in range(1, N+1):
    ans = 'YES'
    S = input().upper()
    # for i in range(len(S)//2):
    #     if S[i] == S[len(S)-i-1]:
    #         continue
    #     else:
    #         ans = 'NO'
    if S != S[::-1]:
        ans = 'NO'
    print('#{} {}'.format(n, ans))
