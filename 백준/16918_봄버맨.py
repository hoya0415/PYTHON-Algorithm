import sys
sys.stdin = open('./16918_input.txt')

def bomb(x, y):
    arr[x][y] = 0
    for k in range(4):
        nx = x + d[k][0]
        ny = y + d[k][1]
        if 0 <= nx < R and 0 <= ny < C:
            arr[nx][ny] = 0

R, C, N = map(int, input().split())
arr = [[0] * C for _ in range(R)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(R):
    C_list = list(input())
    for c in range(C):
        if C_list[c] != '.':
            arr[r][c] = 2
if N > 1:
    for g in range(2, N%4+5):
        if g % 2:
            bomb_list = []
            for i in range(R):
                for j in range(C):
                    if arr[i][j] == 1:
                        bomb_list.append((i, j))
            for b in bomb_list:
                bomb(*b)
        else:
            for i in range(R):
                for j in range(C):
                    if arr[i][j] == 0:
                        arr[i][j] = 3
        for i in range(R):
            for j in range(C):
                if arr[i][j] >= 2:
                    arr[i][j] -= 1
for r in range(R):
    for c in range(C):
        if arr[r][c] == 0:
            arr[r][c] = '.'
        else:
            arr[r][c] = 'O'
    print(''.join(arr[r]))
