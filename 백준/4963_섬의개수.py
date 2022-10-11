import sys
sys.stdin = open('./4963_input.txt')
from collections import deque

def dfs(x, y):
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        vis[a][b] = 1
        for k in range(8):
            na = a + d[k][0]
            nb = b + d[k][1]
            if 0 <= na < N and 0 <= nb < M and vis[na][nb] == 0 and land_map[na][nb] == 1 and (na, nb) not in q:
                q.append((na, nb))

# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
while True:
    M, N = map(int, input().split())
    if N == M == 0:
        break
    land_map = [list(map(int, input().split())) for _ in range(N)]
    vis = [[0] * (M) for _ in range(N)]
    land_cnt = 0

    for i in range(N):
        for j in range(M):
            if land_map[i][j] == 1 and vis[i][j] == 0:
                dfs(i, j)
                land_cnt += 1


    print(land_cnt)