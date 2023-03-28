# 뒤집은 소수

# N개의 자연수를 뒤집은 수가 소수이면 출력
# 단, 910이면 19로 숫자화해야함 (첫자리부터 연속된 0은 무시)
# 뒤집는 함수 reverse(x), 소수판별함수 isPrime(x) 반드시 작성

import sys
# sys.stdin = open('in3.txt', 'rt')

N = int(input())
arr = list(map(int, input().split()))
# print(arr)


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x //= 10
    return res


def isPrime(N):
    res = []
    if N == 1:
        return False
    for i in range(2, N//2+1):
        if N % i == 0:
            return False
    else:
        return True
    # return False
    # else:
    # return True


for a in arr:
    A = reverse(a)
    # print('A', A)
    if isPrime(A):
        print(A, end=' ')
