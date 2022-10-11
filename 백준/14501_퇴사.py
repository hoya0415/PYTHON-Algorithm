import sys
sys.stdin = open('./14501_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_arr = [0] * (N+1)

for i in range(N-1, -1, -1):
    if N >= i + arr[i][0]:
        max_arr[i] = max(max_arr[i+1], arr[i][1] + max_arr[i+arr[i][0]])
    else:
        max_arr[i] = max_arr[i+1]

print(max_arr[0])