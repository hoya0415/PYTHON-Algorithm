import sys
sys.stdin = open('./11724_input.txt')


N, M = map(int, input().split())
U = [[] for _ in range(N+1)]
visit = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    U[u].append(v)
    U[v].append(u)

res = 0

def check(r):
    for c in U[r]:
        if visit[c] == 0:
            visit[c] = 1
            check(c)

for i in range(1, N+1):
    if not visit[i]:
        res += 1
        visit[i] = 1
        check(i)

print(res)