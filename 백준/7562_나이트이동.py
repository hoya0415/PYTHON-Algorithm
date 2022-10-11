import sys
sys.stdin = open('./7562_input.txt')
from collections import deque

def bfs(a, b):
    q = deque([(a, b)])
    res = 0
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if [nx, ny] == M:
                res = visited[x][y] + 1
                break
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and (nx, ny) not in q:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
        if res > 0:
            break
    return res

T = int(input())
d = [[-1, -2], [-2, -1],[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    M = list(map(int, input().split()))
    if S == M:
        print(0)
    else:
        visited = [[0] * N for _ in range(N)]
        print(bfs(*S))