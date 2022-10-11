import sys
sys.stdin = open('./11725_input.txt')
sys.setrecursionlimit(10**6)

def dfs(start):
    for s in V[start]:
        if parents[s] == 0:
            parents[s] = start
            dfs(s)

N = int(input())
V = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

dfs(1)

for p in parents[2:]:
    print(p)