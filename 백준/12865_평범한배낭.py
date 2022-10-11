import sys
sys.stdin = open('./12865_input.txt')

N, K = map(int, input().split())
arr = []

for _ in range(N):
    w, v = map(int, input().split())
    if w <= K and v != 0:
        arr.append((w, v))

dp = []

for i in range(len(arr)):
    dp.append(([i], arr[i][0], arr[i][1]))

for i in range(len(arr)-1):
    ws = dp[i][0]
    w = dp[i][1]
    v = dp[i][2]
    for j in range(i+1, len(dp)):
        if j != i and w + dp[j][1] <= K:
            j0 = ws + dp[j][0]
            flag = 1
            for b in dp[j][0]:
                if b in ws:
                    flag = 0
            if flag:
                dp.append((j0, dp[j][1] + w, dp[j][2] + v))

print(dp[-1][2], dp)
# res = 0
#
# for i in range(len(dp)):
#     if dp[i][2] > res:
#         res = dp[i][2]



