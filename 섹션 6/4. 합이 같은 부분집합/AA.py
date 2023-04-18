# 합이 같은 부분집합 (아마존 인터뷰: DFS)

# N개의 원소로 구성된 자연수 집합이 주어진다.
# 이 집합을 2개의 부분집합으로 나누었을 때
# 두 부분집합 원소의 합이 서로 같은 경우가 존재하면 YES 아니면 NO

# 둘로 나뉘는 두 부분집합은 서로소집합이며, 합하면 입력으로 주어진 원래 집합이 돼야 한다.
# * 서로소집합: 공통원소가 없는 두 집합
# 예)
# 입력: {1, 3, 5, 6, 7, 10}
# => {1, 3, 5, 7}, {6, 10} 으로 두 부분집합의 합이 같다
import sys


def DFS(v, tot):
    global total
    if v == N:
        # 배열 전체 합에서 부분집합 합을 뺀 게 부분집합 합과 같으면 예뜨
        if tot == total - tot:
            print('YES')
            sys.exit(0)   # 프로그램 종료
        return
    else:
        DFS(v+1, tot+arr[v])
        DFS(v+1, tot)
    return


N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)  # 배열 전체 합
DFS(0, 0)
print('NO')       # 프로그램 종료 안 거치면 no 출력
