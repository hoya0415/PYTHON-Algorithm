import sys
sys.stdin = open('./1697_input.txt')

N, K = map(int, input().split())

if N + 1 < K:
    arr = [987654321] * (K+4)
    arr[N] = 0
    arr[N-1] = 1
    arr[N+1] = 1
    for i in range(N):
        arr[i] = N-i
    for i in range(N+1+(N%2), K+2, 2):
        if (i + 1) // 2 >= 0:
            arr[i + 1] = min(arr[(i + 1) // 2], arr[i + 2], arr[i-1]+1) + 1
        else:
            arr[i + 1] = arr[i-1] + 2
        arr[i] = min(arr[i - 1], arr[i + 1]) + 1
    print(arr[K])
else:
    print(abs(N-K))