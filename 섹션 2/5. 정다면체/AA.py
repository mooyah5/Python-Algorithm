# 정다면체

# 정N면체, 정M면체 주사위를 던져 나오는 눈의 합 중 확률이 높은 숫자
# 여러 정답이면 오름차 출력

import sys
from collections import Counter
# sys.stdin = open('in2.txt', 'rt')
N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    for j in range(1, M+1):
        arr.append(i + j)
cnt = Counter(arr).most_common()  # 카운팅(요소, 요소개수)해주고, 오름차순정렬
maxcnt = cnt[0][1]                # 가장 큰 첫번째 요소의 개수
for c in cnt:                     # 모든 cnt를 돌아서
    if maxcnt == c[1]:            # 가장 큰 요소의 개수와 동일한 요소를 출력
        print(c[0], end=' ')
