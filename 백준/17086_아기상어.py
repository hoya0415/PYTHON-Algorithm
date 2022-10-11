import sys
sys.stdin = open('./17086_input.txt')
from collections import deque

def bfs(a, b):
    global res
    q = deque([(a, b, 0)])
    visit = [[0]*M for _ in range(N)]
    while q:
        x, y, cnt = q.popleft()
        if visit[x][y] == 1:
            continue
        else:
            visit[x][y] = 1
            for k in range(8):
                nx = x + d[k][0]
                ny = y + d[k][1]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    if arr[nx][ny] == 1:
                        if res < cnt+1:
                            res = cnt+1
                        return
                    q.append((nx, ny, cnt+1))

d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(i, j)

print(res)