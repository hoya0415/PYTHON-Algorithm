import sys
sys.stdin = open('./2468_input.txt')
from collections import deque

def check(h, i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] > h and (nx, ny) not in q:
                q.append((nx, ny))

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(input())
min_h = 987654321
max_h = 0
arr = []
res = 1

for _ in range(N):
    lst = list(map(int, input().split()))
    if min_h > min(lst):
        min_h = min(lst)
    if max_h < max(lst):
        max_h = max(lst)
    arr.append(lst)

for h in range(min_h, max_h):
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visit[i][j] == 0:
                check(h, i, j)
                cnt += 1

    if res < cnt:
        res = cnt

print(res)