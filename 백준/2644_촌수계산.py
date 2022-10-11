import sys
sys.stdin = open('./2644_input.txt')
from collections import deque


N = int(input())
X, Y = map(int, input().split())
M = int(input())
arr = [[] for _ in range(N + 1)]
visited = [0] * (N+1)

for i in range(M):
    o, p = map(int, input().split())
    arr[o].append(p)
    arr[p].append(o)

q = deque([(X, 1)])
res = -1
while q:
    x, cnt = q.popleft()
    visited[x] = 1
    for i in arr[x]:
        if i == Y:
            res = cnt
            break
        elif visited[i] == 0:
            q.append((i, cnt+1))
    if res == cnt:
        break

print(res)
