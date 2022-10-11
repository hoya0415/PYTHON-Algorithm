import sys
sys.stdin = open('./15486_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i == N - 1:
        pv = 0
    else:
        pv = dp[i + 1]
    if arr[i][0] <= N-i:
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], pv)
    else:
        dp[i] = pv
print(dp[0])