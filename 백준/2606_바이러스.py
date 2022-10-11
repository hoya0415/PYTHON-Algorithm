import sys
sys.stdin = open('2606_input.txt')

def search(v):
    for i in range(1, C + 1):
        if arr[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            search(i)

C = int(input())
N = int(input())
arr = [[0] * (C+1) for _ in range(C+1)]
visited = [0] * (C+1)

for _ in range(N):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

search(1)

# print(visited)
print(visited.count(1)-1)





