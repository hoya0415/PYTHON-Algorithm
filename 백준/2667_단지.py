import sys
sys.stdin = open('./2667_input.txt')
from collections import deque

def dfs(x, y):
    cnt = 0
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        visited[a][b] = 1
        cnt += 1
        for k in range(4):
            na = a + d[k][0]
            nb = b + d[k][1]
            if 0 <= na < N and 0 <= nb < N and visited[na][nb] == 0 and vill[na][nb] == 1 and (na, nb) not in q:
                q.append((na, nb))
    res.append(cnt)

N = int(input())
vill = [[] * (N) for _ in range(N)]
visited = [[0] * (N) for _ in range(N)]
res = []
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    vill[i] = list(map(int, input()))

for i in range(N):
    for j in range(N):
        if vill[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)

print(len(res))
for r in sorted(res):
    print(r)
