# 이항계수

# 경우의 수 계산 시 사용하는 것으로,
# n 개의 서로 다른 것들 중, k개를 선택하는 것의 조합의 경우의 수

# ( n )
# ( k )
# 는 nCk 조합으로 나타낼 수 있다.

# nCk => factorial(n) // (factorial(k) * factorial(n-k))
# nCk => n! // k!(n - k!)


### 재귀 풀이
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


### 반복문 풀이
def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


###
n, k = map(int, input().split())
print(factorial(n) // factorial(k) * factorial(n - k))
