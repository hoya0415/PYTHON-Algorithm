import sys
sys.stdin = open('./1018_input.txt')

def check(x, y, t):
    tmp = t
    cnt = 0
    for r in range(x, x + 8):
        for c in range(y, y + 8):
            if arr[r][c] == tmp:
                cnt += 1
            if tmp == 'W':
                tmp = 'B'
            else:
                tmp = 'W'
        if tmp == 'W':
            tmp = 'B'
        else:
            tmp = 'W'
    if cnt > 32:
        return 64 - cnt
    else:
        return cnt

res = 32
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        c = check(i, j, arr[i][j])
        if c < res:
            res = c
        if res == 0:
            break
    if res == 0:
        break

print(res)
