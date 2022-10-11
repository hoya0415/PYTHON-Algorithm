import sys
sys.stdin = open('./11403_input.txt')

def check(s, c, y):
    visit[c] = 1
    for j in range(N):
        if arr[c][j] == 1 and c != j:
            if j == y:
                return 1
            elif j != s:
                if res[j][y] == 1:
                    return 1
                if not visit[j]:
                    if check(s, j, y):
                        return 1
    return 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            res[i][j] = 1
        else:
            visit = [0] * N
            res[i][j] = check(i, i, j)

for r in res:
    print(*r)
