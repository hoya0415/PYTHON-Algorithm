import sys
sys.stdin = open('./1463_input.txt')


N = int(input())
arr = [0] * (N+1)

for i in range(2, N+1):
    a = i // 3
    b = i // 2
    c = i - 1
    min_v = 987654321

    if i % 3 == 0 and arr[a] < min_v:
        min_v = arr[a]
    if i % 2 == 0 and arr[b] < min_v:
        min_v = arr[b]
    if arr[c] < min_v:
        min_v = arr[c]

    arr[i] = min_v + 1

print(arr[N])