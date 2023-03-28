# 대표값

# N명의 학생들의 점수 평균(소수 첫째자리 반올림)에서 가까운 학생 번호
# 여러 개면 점수가 높을수록, 여러 명이면 번호가 빠를수록
import sys
# sys.stdin = open('in1.txt', 'rt')
N = int(input())  # 학생 수
arr = list(map(int, input().split()))
ave = int(sum(arr) + 0.5)
min = float('inf')
for idx, a in enumerate(arr):
    tmp_min = abs(ave-a)    # 평균에서 점수값을 뺀 절대값
    if tmp_min < min:       # 현재 뺀 값이 최소값보다 작으면
        min = tmp_min       # 최소값을 갱신하고
        score = a           # 그 점수를 저장해두고
        res = idx           # 그 점수의 인덱스(학생번호)도 저장해둠
    elif tmp_min == min:    # 현재 뺀 값이 최소값과 같으면
        if score < a:       # 그 점수가 더 높으면
            score = a
            res = idx
print(ave, res+1)
