import sys
sys.stdin = open('2606_input.txt')

def dfs(start):
    for s in V[start]:
        if not visited[s]:
            visited[s] = 1
            dfs(s)

N = int(input())
L = int(input())
V = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(L):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

visited[1] = 1
dfs(1)

print(sum(visited) - 1)