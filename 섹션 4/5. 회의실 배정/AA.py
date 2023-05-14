# 회의실 배정 (그리디)

N = int(input())
meeting = [list(map(int, input().split())) for i in range(N)]
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
end_time = 0  # 현재 회의했던 회의가 끝나는 시간
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)
