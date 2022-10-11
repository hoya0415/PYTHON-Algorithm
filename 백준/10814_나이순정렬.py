import sys
sys.stdin = open('./10814_input.txt')

N = int(input())
arr = []

for i in range(N):
    n, name = input().split()
    arr.append((i, int(n), name))

arr.sort(key=lambda x:(x[1], x[0]))

for i, n, name in arr:
    print(n, name)