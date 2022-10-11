import sys
sys.stdin = open('13300_input.txt')

N, K = map(int, input().split())
arr = [0] * 13
cnt = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        arr[Y] += 1
    else:
        arr[Y+6] += 1

for a in range(1, 13):
    if arr[a] > 0:
        cnt += arr[a] // K
        if arr[a] % K > 0:
            cnt += 1

print(cnt)