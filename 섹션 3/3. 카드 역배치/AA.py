# 카드 역배치

# 1~20 숫자가 쓰인 20장의 카드가 오름차순 한줄로 놀여있다.
# 총 10개의 구간 a, b가 주어지면 역순으로 놓아 마지막 배치를 출력

# import sys
# sys.stdin = open('in1.txt', 'rt')
arr = [i for i in range(21)]
# print(arr)
for tc in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
print(*arr[1::])
