import sys
sys.stdin = open('./18428_input.txt')

def d_check(x, y, k, p):
    global flag
    nx = x + d[k][0]
    ny = y + d[k][1]
    if 0 <= nx < N and 0 <= ny < N:
        if arr[nx][ny] == 'X':
            p.append((nx, ny))
            d_check(nx, ny, k, p)
        elif arr[nx][ny] == 'T':
            lst.append(p)
            return

def check(x, y):
    global flag
    for k in range(4):
        p = []
        nx = x + d[k][0]
        ny = y + d[k][1]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 'X':
                p.append((nx, ny))
                d_check(nx, ny, k, p)
            elif arr[nx][ny] == 'T':
                if len(p) == 0:
                    flag = 1
                    return
                lst.append(p)



N = int(input())
arr = []
lst = []
flag = 0
res = 'NO'
# 좌, 우, 상, 하
d = [(0, -1), (0, 1),(-1, 0), (1, 0)]


for _ in range(N):
    arr.append(list(input().split()))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':

            check(i, j)
            if flag == 1:
                break
    if flag == 1:
        break

if flag == 0:
    if len(lst) <= 3:
        res = 'YES'
    else:
        cnt = 0
        for i in range(len(lst)):
            for l in lst[i]:
                for j in range(i+1, len(lst)):
                    if l in lst[j]:
                        cnt += 1
        if len(lst)-cnt <= 3:
            res = 'YES'

print(res)