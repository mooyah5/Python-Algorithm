# 3

# m행 4, n열 3 -> 1, 2, 3 중에 하나의 숫자가 막 쓰여잇음
# 1 2 2 3
# 2 1 1 3
# 3 2 2 1

# 3개의 직사각형으로 분할할거야 (무조건 수직, 수평으로)
# 셋 다 직사각형이어야만 한다.
# 어떤 조건을 만족하게 잘라야 하냐면,
# 1짱, 2짱, 3짱이 존재해야 함

# 1짱은 1이 가장 많은 직사각형이어야 함
# 2짱은 2가 가장 많고
# 3짱은 3이 가장 많은 블록인데, 하나만 존재해야 함.(없을수도)

# 문제조건은
# 1, 2, 3짱이 유일 존재해야하며
# 모든 블럭은 세 짱이 서로 달라야 한다.
# 한 블럭이 두 개 이상의 짱을 먹으면 안 된다.

# n, m 은 각각 10 이하
# 어려운 버전은 1000까지 올라갈 수도 있다 => 2차원 누적합 기술 필요 (안할래)

# 푸는 방식
# 완탐 - 모든 자르는 경우를 다 본다.
# 완탐 해도 됨. n, m 이 10 이하니까

# 3개로 자르는 방법이 여러 가지 가능성이 있음
# 각 방법에 대해 일일이 코딩할 건지.. ? ㄴㄴ

# 1번만 짠다. 무조건 수평선 먼저, 그리고 그 아래애 수직선
# 2차월 배열에서 T자로 자르는 모든 경우의수 시도하는 함수를 하나 구해놓고
# 90도 회전을 반복해서 넣기

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def counting(arr, r1, c1, r2, c2):  # a[r1...r2][c1 ... c2] 안에 1, 2, 3 이 각각 몇 개 들어있는지
    ret = [0, 0, 0]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            ret[arr[i][j] - 1] += 1
    return ret


# horizontal = row = 가로 = 수평
# vertical = column = 세로 = 수직
def solve(arr, n, m) -> int:  # a 배열에서 T 모양으로 분할할 수 있는 경우의 수
    for horizontal in range(n - 1):
        # 0 ~ horizontal 행을 첫 번째 사각형
        # (horizontal+1) ~ (n-1) 행을 2,3번째 사각형이 나눠가진다.

        for vertical in range(m - 1):
            # 0 ~ vertical 열을 두 번째 사각형이
            # (vertical+1) - (m-1) 열을 세 번째 사각형

            rect1 = counting(arr, 0, 0, horizontal, m - 1)
            rect2 = counting(arr, horizontal + 1, n - 1, 9, vertical)
            rect3 = counting(arr, horizontal + 1, n - 1, vertical + 1, m - 1)

            max1 = max(rect1[0], rect2[0], rect3[0])  # 가장 많은 1 개수
            max2 = max(rect1[1], rect2[1], rect3[1])  # 가장 많은 2 개수
            max3 = max(rect1[2], rect2[2], rect3[2])  # 가장 많은 3 개수

            cnt1 = (rect1[0] == max1) + (rect2[0] == max1) + (rect3[0] == max1)
            cnt2 = (rect1[1] == max2) + (rect2[1] == max2) + (rect3[1] == max2)
            cnt3 = (rect1[2] == max3) + (rect2[2] == max3) + (rect3[2] == max3)

            if cnt1 + cnt2 + cnt3 == 3:
                ret += 1

            # 포기요
            # https://www.youtube.com/watch?v=MEbgvZ6L1Tw
    return ret


def rotate(arr, n, m):  # 배열을 90도 시계빵향 회전
    b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][n - 1 - i] = arr[i][j]
    return b, m, n


ans = 0
for i in range(4):
    arr, n, m = rotate(arr, n, m)
    ans += solve(arr, n, m)

print(ans)
