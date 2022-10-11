import sys
sys.stdin = open('./1986_input.txt')

N, M = map(int, input().split())
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
arr = [[0]*M for _ in range(N)]
qd = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
kd = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

for i in range(1, p[0]*2, 2):
    x, y = p[i]-1, p[i+1]-1
    arr[x][y] = 4

for i in range(1, k[0]*2, 2):
    x, y = k[i]-1, k[i+1]-1
    arr[x][y] = 3
    for f in range(8):
        nx = x + kd[f][0]
        ny = y + kd[f][1]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1

for i in range(1, q[0]*2, 2):
    x, y = q[i]-1, q[i+1]-1
    arr[x][y] = 2
    for f in range(8):
        fx, fy = x, y
        while True:
            nx = fx + qd[f][0]
            ny = fy + qd[f][1]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] < 2:
                    arr[nx][ny] = 1
                    fx, fy = nx, ny
                else:
                    break
            else:
                break
print(arr)
res = 0
for a in arr:
    res += a.count(0)

print(res)