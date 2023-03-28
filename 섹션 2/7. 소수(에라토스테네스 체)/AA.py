# 소수 (에라토스테네스 체)

# 에라토스테네스의 체
# 2, 3, 5, 7 ...는 소수이되 그 배수는 소수가 아님

# 자연수 N의 소수의 개수 출력
import sys
# sys.stdin = open('in2.txt', 'rt')
N = int(input())
ch = [0] * (N+1)
cnt = 0

for i in range(2, N+1):
    if ch[i] == 0:  # 0이면 소수
        cnt += 1
        for j in range(i, N+1, i):    # i부터 i의 배수씩 증가
            ch[j] = 1  # 소수가 아님을 체크
print(cnt)
