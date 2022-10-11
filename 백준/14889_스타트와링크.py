import sys
sys.stdin = open('./14889_input.txt')
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 987654321

for comb in combinations(range(N), N//2):
    start = 0
    link = 0
    comb_x = list(range(N))
    for a, b in combinations(comb, 2):
        start += arr[a][b] + arr[b][a]
        if a in comb_x:
            comb_x.remove(a)
        if b in comb_x:
            comb_x.remove(b)
    for a, b in combinations(comb_x, 2):
        link += arr[a][b] + arr[b][a]
    if abs(start - link) < res:
        res = abs(start - link)
        if res == 0:
            break

print(res)





