import sys
sys.stdin = open('./1189_input.txt')

def dfs(x, y, cnt):
    global res, visited
    visited[x][y] = cnt
    for k in range(4):
        nx = x + d[k][0]
        ny = y + d[k][1]

        if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and arr[nx][ny] != 'T' and cnt < N:
            if (nx, ny) == (0, C - 1):
                if cnt + 1 == N:
                    res += 1
                continue
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0

R, C, N = map(int, input().split())
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = []
res = 0
visited = [[0] * C for _ in range(R)]
for _ in range(R):
    arr.append(list(input()))

dfs(R-1, 0, 1)
print(res)
