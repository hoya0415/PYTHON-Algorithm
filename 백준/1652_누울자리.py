import sys
sys.stdin = open('1652_input.txt')

N = int(input())
arr = [list(input()) for _ in range(N)]
r_ans = 0
c_ans = 0

for i in range(N):
    r = []
    for j in range(N):
        if arr[i][j] == '.':
            r.append(arr[i][j])
        elif arr[i][j] == 'X':
            if len(r) >= 2:
                r_ans += 1
            r = []
    if len(r) >= 2:
        r_ans += 1


for i in range(N):
    c = []
    for j in range(N):
        if arr[j][i] == '.':
            c.append(arr[j][i])
        if arr[j][i] == 'X':
            if len(c) >= 2:
                c_ans += 1
            c = []
    if len(c) >= 2:
        c_ans += 1

print(r_ans, c_ans)