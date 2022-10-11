import sys
sys.stdin = open('./24444_input.txt')
from collections import deque

N, M, R = map(int, input().split())
V = [[] for _ in range(N+1)]
visited = [0] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())
    V[u].append(v)
    V[v].append(u)
    
for j in range(N+1):
    V[j].sort()

def bfs(V, visited, R):
    q = deque([R])
    visited[R] = 1
    cnt = 2
    
    while q:
        r = q.popleft()
        
        for i in V[r]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = cnt
                cnt += 1
    
    
bfs(V, visited, R)

for i in visited[1::]:
    print(i)


