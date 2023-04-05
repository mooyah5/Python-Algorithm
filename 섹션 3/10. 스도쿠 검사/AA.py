# 스도쿠 검사

# 스도쿠대로 각 행, 각 열, 3*3 크기 보드에 중복 없이 나타나도록
# 입력으로 완성된 스도쿠가 주어진다. 잘 풀었으면 예쓰, 틀리면 노 출력

def check(arr):
    for i in range(9):
        nums1 = [0]*10        # 행
        nums2 = [0]*10        # 열
        for j in range(9):
            nums1[arr[i][j]] = 1
            nums2[arr[i][j]] = 1
        if sum(nums1) != 9 or sum(nums2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            nums3 = [0] * 10   # 3*3
            for k in range(3):
                for s in range(3):
                    nums3[arr[i*3+k][j*3+s]] = 1
            if sum(nums3) != 9:
                return False
    return True


arr = [list(map(int, input().split())) for i in range(9)]
if check(arr):
    print('YES')
else:
    print('NO')
