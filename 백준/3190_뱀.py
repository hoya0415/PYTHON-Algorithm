import sys
sys.stdin = open('./3190_input.txt')

from collections import deque
sys.setrecursionlimit(10**6)

def snake(x, y):
    global idx, k, sec
    sec += 1
    nx = x + d[k][0]
    ny = y + d[k][1]

    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in sn:
        sn.append((nx, ny))
        if arr[nx][ny] == 1:
            arr[nx][ny] = 0
        else:
            sn.popleft()
        if idx < L:
            if int(l_lst[idx][0]) == sec:
                if l_lst[idx][1] == 'L':
                    k = (k - 1) % 4
                else:
                    k = (k + 1) % 4
                idx += 1
        snake(nx, ny)
    else:
        return

N = int(input())
K = int(input())
sec = 0
sn = deque([])
sn.append((0, 0))
arr = [list([0] * N) for _ in range(N)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

L = int(input())
l_lst = []

for l in range(L):
    i, dir = input().split()
    l_lst.append((i, dir))

idx = 0
k = 0

snake(0, 0)
print(sec)