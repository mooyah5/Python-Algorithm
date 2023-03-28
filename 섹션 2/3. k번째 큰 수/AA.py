# k번째 큰 수

# N 장의 카드에 1~100 사이 자연수가 적혀있음 (중복 가능)
# 3장을 뽑아 합할 수 있는 모든 경우의 수 중 k번째로 큰 수
import sys
# sys.stdin = open('in4.txt', 'rt')
N, K = map(int, input().split())
arr = list(map(int, input().split()))
new = set()
leng = len(arr)
for i in range(leng-2):
    for j in range(i+1, leng-1):
        for k in range(j+1, leng):
            if i != j and j != k and k != i:
                new.add(arr[i]+arr[j]+arr[k])
sortedArr = sorted(list(new), reverse=True)
# print(new)
print(sortedArr[K-1])
