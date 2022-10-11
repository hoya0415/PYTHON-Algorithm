import sys
sys.stdin = open('./2156_input.txt')

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0] * N

for i in range(N):
    v1 = v2 = v3 = v4 = 0
    if i > 0:
        v1 = dp[i-1]
        v4 = arr[i-1] + arr[i]
    if i > 1:
        v2 = dp[i-2] + arr[i]
    if i > 2:
        v3 = dp[i-3] + arr[i-1] + arr[i]
    dp[i] = max(v1, v2, v3, v4, arr[i])

print(max(dp))