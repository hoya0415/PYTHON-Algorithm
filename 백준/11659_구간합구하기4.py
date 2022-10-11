import sys
sys.stdin = open('./11659_input.txt')

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sum_arr = [0] * (N+1)

for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]

for _ in range(M):
    a, b = sorted(map(int, input().split()))
    print(sum_arr[b] - sum_arr[a-1])