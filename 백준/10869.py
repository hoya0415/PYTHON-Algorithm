from itertools import permutations
import sys
sys.stdin = open('10869_input.txt')
from collections import deque

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visit = [0] * N
q = deque([R])
visit[R-1] = 1
sun = 2

while q:
    for i in sorted(arr[q.popleft()]):
        if visit[i-1] == 0:
            q.append(i)
            visit[i-1] = sun
            sun += 1

print(*visit, sep='\n')
