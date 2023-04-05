# 숫자만 추출

# 문자, 숫자가 섞인 문자열에서 숫자만 추출하여 그 순서대로 자연수를 만든다.
# 만들어진 자연수와 그 자연수의 약수 개수를 출력한다.
# import sys
# sys.stdin = open('in4.txt', 'rt')
S = input()
newS = ''
ans = 0
for s in S:
    if s.isdigit():  # isdemical(0~10)
        newS += s
        # ans = ans * 10 + int(s)
newS = int(newS)
print(newS)
res = 0
for i in range(1, newS+1):
    if newS % i == 0:
        res += 1
print(res)
