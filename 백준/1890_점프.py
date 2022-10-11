import sys
sys.stdin = open('./1890_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == j == N-1:
            print(dp[i][j])
        cur = arr[i][j]
        if j + cur < N:
            dp[i][j + cur] += dp[i][j]
        if i + cur < N:
            dp[i + cur][j] += dp[i][j]

