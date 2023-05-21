#### 정방형 2차원 배열 90도 회전하기

# 회전 전의 열, 회전 후의 행이 일치한다.
# 따라서 두 곳에 y값을 그대로 준다.

# 회전 후의 열 = N-1에서 회전 전의 행을 뺀 값이다.
# 회전 전의 행 번호가 x일 때, N-1에서 y값을 빼주기

### 1) 90도 회전 1  ###################


# def rotate_90(ago):
#     N = len(ago)
#     M = len(ago[0])

#     res = [[0] * N for _ in range(M)]
#     for x in range(N):
#         for y in range(M):
#             res[y][N - 1 - x] = ago[x][y]
#             # res[0,1,2][2, 1, 0] = ago[0,1,2][0,1,2]
#     return res


# test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(rotate_90(test))


### 2) 90도 회전 2 ###################


def rotate_90_2(ago):
    reversed_ = ago[::-1]
    res = list(map(list, zip(*reversed_)))  # 전치 (Transposition)
    return res


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_90_2(test))


### 3) 180도 회전 ###################


def rotate_180(ago):
    N = len(ago)
    res = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            res[N - 1 - y][N - 1 - x] = ago[x][y]
    return res
