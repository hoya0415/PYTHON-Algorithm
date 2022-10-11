import sys
sys.stdin = open('./17626_input.txt')

N = int(input())
arr = [0] * (N+1)
arr[1] = 1
for i in range(2, N+1):
    cnt = 1
    res = 4
    while cnt ** 2 <= i:
        res = min(res, arr[i - cnt ** 2])
        cnt += 1
    arr[i] = res + 1

print(arr[N])
