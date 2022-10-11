import sys
sys.stdin = open('./11048_input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        lt = t = l = 0
        if 0 <= i-1 < N and 0 <= j-1 < M:
            lt = dp[i-1][j-1]
        if 0 <= i-1 < N:
            l = dp[i-1][j]
        if 0 <= j-1 < M:
            t = dp[i][j-1]
        dp[i][j] = max(lt + arr[i][j], l + arr[i][j], t + arr[i][j])

print(dp[N-1][M-1])