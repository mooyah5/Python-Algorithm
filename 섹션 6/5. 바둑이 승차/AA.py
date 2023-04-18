# 바둑이 승차 (DFS)

# 철수가 바둑이들 데꼬 시장 갈 거임.
# 근데 트럭에 C kg 넘게 못 태움.
# C를 안 넘기면서 바둑이들을 가장 무겁게 태우고 싶다.

# 최대무게 C, N마리 바둑이, 각 바둑이 무게 W가 주어지면,
# 가장 무겁게 태울 수 있는 무게 구하기

# # 1. Time Limit Exceeded
# def DFS(i, kg):
#     global largest
#     if i == N:                          #
#         if kg <= C and largest < kg:
#             largest = kg
#         return
#     else:
#         if kg+arr[i] > C:
#             pass
#         else:
#             DFS(i+1, kg+arr[i])
#         DFS(i+1, kg)
#     return


# C, N = map(int, input().split())        # 최대허용무게, 바둑이마릿수
# arr = [int(input()) for i in range(N)]  # 바둑이들 몸무게
# largest = -1                            # 출력할 무게 합 최대
# DFS(0, 0)                               # DFS(arr의 인덱스, 무게합)
# print(largest)

# 2. 가지치기
def DFS(i, kg, remain_kg):
    global largest, total
    if kg + total - remain_kg < largest:
        return
    if i == N:                          #
        if kg <= C and largest < kg:
            largest = kg
        return
    else:
        DFS(i+1, kg+arr[i], remain_kg+arr[i])
        DFS(i+1, kg, remain_kg+arr[i])
    return


C, N = map(int, input().split())        # 최대허용무게, 바둑이마릿수
arr = [int(input()) for i in range(N)]  # 바둑이들 몸무게
largest = -1                            # 출력할 무게 합 최대
total = sum(arr)
DFS(0, 0, 0)                            # DFS(arr의 인덱스, 무게합, 가지치기)
print(largest)
