import sys
sys.stdin = open('1012_input.txt')
sys.setrecursionlimit(10**6)

def search(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and farm[nx][ny] == 1:
            search(nx, ny)

T = int(input())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(T):
    N, M, K = map(int, input().split())
    farm = [[0] * M for _ in range(N+1)]

    for _ in  range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    visited = [[0] * M for _ in range(N+1)]
    res = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] != 1:
                res += 1
                search(i, j)
            if res >= K:
                break
        if res >= K:
            break

    print(res)

