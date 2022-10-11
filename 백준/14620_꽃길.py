import sys
sys.stdin = open('./14620_input.txt')

def check(x, y):
    v = 0
    for k in range(5):
        nx = x+d[k][0]
        ny = y+d[k][1]
        v += arr[nx][ny]
    return v

d = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 20000

for i in range(1, N-1):
    for j in range(1, N-1):
        v1 = check(i, j)
        for r in range(1, N-1):
            for c in range(1, N-1):
                if abs(r - i) + abs(c - j) < 3:
                    continue
                v2 = check(r, c)
                for h in range(1, N-1):
                    for g in range(1, N-1):
                        if abs(h - r) + abs(g - c) < 3 or abs(h - i) + abs(g - j) < 3:
                            continue
                        v3 = check(h, g)
                        if v1 + v2 + v3 < res:
                            res = v1 + v2 + v3

print(res)