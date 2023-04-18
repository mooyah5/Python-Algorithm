# 재귀함수 이진수 출력

# 10진수 N이 입력되면 2진수로 변환하여 출력

def binary(N):
    global ans
    A, B = N // 2, N % 2
    ans.insert(0, B)
    if A < 2:
        ans.insert(0, A)
        return
    else:
        return binary(A)


N = int(input())
ans = []
binary(N)
# for a in ans:
print(''.join(list(map(str, ans))))
