import sys
sys.stdin = open('./15686_input.txt')
from itertools import combinations

N, M = map(int, input().split())
zido = [[0] * N for _ in range(N)]
chick = []
home = []
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        zido[i][j] = lst[j]
        if lst[j] == 1:
            home.append((i, j))
        elif lst[j] == 2:
            chick.append((i, j))

res = 987654321
for comb in combinations(chick, M):
    comb_res = 0
    for h in home:
        min_dis = 987654321
        for c in comb:
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            if dis < min_dis:
                min_dis = dis
        comb_res += min_dis
    if comb_res < res:
        res = comb_res

print(res)
