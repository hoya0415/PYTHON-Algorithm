import sys
sys.stdin = open('./9205_input.txt')
from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    X, Y = map(int, input().split())
    n_list = [tuple(map(int, input().split())) for _ in range(N)]
    n_list_visit = [0] * (N + 1)
    n_list.append((X, Y))
    FX, FY = map(int, input().split())
    res = 'sad'
    q = deque([(X, Y)])
    while q and res == 'sad':
        x, y = q.popleft()
        n_list_visit[n_list.index((x, y))] = 1
        if abs(FX-x) + abs(FY-y) <= 1000:
            res = 'happy'
            break
        for nx, ny in n_list:
            if abs(x-nx) + abs(y-ny) <= 1000 and (nx, ny) not in q and n_list_visit[n_list.index((nx, ny))] == 0:
                if abs(FX-nx) + abs(FY-ny) <= 1000:
                    res = 'happy'
                    break
                q.append((nx, ny))

    print(res)