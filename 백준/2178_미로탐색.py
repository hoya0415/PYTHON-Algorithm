import sys
sys.stdin = open('./2178_input.txt')
from collections import deque

def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and (nx, ny) not in q and arr[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                if (nx, ny) == (N-1, M-1):
                    return
                q.append((nx, ny))


d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]
bfs(0, 0)

print(visited[N-1][M-1])
