import sys
sys.stdin = open('./2583_input.txt')
from collections import deque

def check(i, j):
    res = 1
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and (nx, ny) not in q:
                res += 1
                q.append((nx, ny))
    return res

M, N, K = map(int, input().split())
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [[0] * M for _ in range(N)]
cnt = 0
young = []

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            visit[i][j] = 1

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            cnt += 1
            young.append(check(i, j))

print(cnt)
print(*sorted(young))