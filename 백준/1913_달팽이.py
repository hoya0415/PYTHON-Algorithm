import sys
sys.stdin = open('./1913_input.txt')

N = int(input())
J = int(input())
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr = [[0] * (N) for _ in range(N)]
x = y = N // 2
k = 0

for i in range(1, N*N+1):
    if i == J:
        res = x+1, y+1
    arr[x][y] = i
    x += d[k][0]
    y += d[k][1]
    nk = (k+1) % 4
    if arr[x + d[nk][0]][y + d[nk][1]] == 0:
        k = nk

for _ in range(N):
    print(*arr[_])
print(*res)

