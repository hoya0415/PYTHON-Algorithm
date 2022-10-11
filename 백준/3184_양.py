import sys
sys.stdin = open('./3184_input.txt')
from collections import deque

def check(i, j):
    global sheep, wolf
    s = w = 0
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        if arr[x][y] == 'o':
            s += 1
        elif arr[x][y] == 'v':
            w += 1
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and (nx, ny) not in q:
                if arr[nx][ny] != '#':
                    q.append((nx, ny))
    if s > w:
        sheep += s
    else:
        wolf += w

N, M = map(int, input().split())
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [[0] * M for _ in range(N)]
arr = [list(input().strip()) for _ in range(N)]
sheep = wolf = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != '#' and not visit[i][j]:
            check(i, j)

print(sheep, wolf)