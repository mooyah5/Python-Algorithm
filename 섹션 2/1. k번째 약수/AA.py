import sys
for tc in range(1, 6):
    print(tc, ')')
    sys.stdin = open('in{0}.txt'.format(tc), 'rt')
    ans = 0
    n, k = map(int, input().split())
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            print(i)
            ans = i
            break
    else:
        ans = -1
        print(-1)

    sys.stdin = open('out{0}.txt'.format(tc), 'rt')
    answer = int(input())
    if answer == ans:
        print(ans, answer, '정답입니다.')
    else:
        print(ans, answer, '틀렸습니다')
