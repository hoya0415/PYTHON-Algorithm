import sys
sys.stdin = open('./1874_input.txt')

N = int(input())
arr = list(range(N, 0, -1))
stack = []
res = []

for _ in range(N):
    n = int(input())
    if not stack or stack[-1] != n:
        if N - len(arr) > n:
            res = ['NO']
            break
        for i in range(N - len(arr), n):
            stack.append(arr.pop())
            res.append('+')
    if stack[-1] == n:
        stack.pop()
        res.append('-')

for r in res:
    print(r)
