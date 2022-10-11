import sys
sys.stdin = open('./1931_input.txt')

N = int(input())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[1], x[0]))
res = e = 0

for a in arr:
    if a[0] >= e:
        res += 1
        e = a[1]

print(res)
