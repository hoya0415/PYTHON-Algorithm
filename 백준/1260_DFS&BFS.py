import sys
sys.stdin = open('./1260_input.txt')

from collections import deque

# DFS 탐색
def dfs(v):
    # 인접리스트 돌면서 방문리스트에 해당 인자 없으면 추가하고 재귀로 바로 DFS탐색
    for i in arr[v]:
        if i not in dfs_visited:
            dfs_visited.append(i)
            dfs(i)

# BFS 탐색
def bfs():
    # 인접 리스트 돌면서 방문 안 한 지점 있으면 방문리스트에 넣고 큐에도 넣기
    while q:
        w = q.popleft()
        for i in arr[w]:
            if i not in bfs_visited:
                bfs_visited.append(i)
                q.append(i)

N, M, V = map(int, input().split())
arr =[[] for _ in range(N+1)] # 인접 리스트

# 인접 리스트 채우기
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 인접 리스트 작은 수부터 방문할 수 있게 정렬
for arg in arr:
    arg.sort()

dfs_visited = [V] # DFS 방문 리스트
bfs_visited = [V] # BFS 방문 리스트
q = deque([V]) # BFS에서 쓸 큐

dfs(V)
bfs()

print(*dfs_visited)
print(*bfs_visited)
