import sys
sys.stdin = open('test1.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    visited = [0] * N
    G1L, G1P = map(int, input().split())
    G2L, G2P = map(int, input().split())
    G3L, G3P = map(int, input().split())
    arr = [(G1L, G1P), (G2L, G2P), (G3L, G3P)]
    min_cnt = 987654321
    cnt = 0
    for i in range(3):
        for j in range(arr[i][1]):
            flag = 0
            cur = arr[i][0]
            while True:
                if visited[cur]==0:
                    visited[cur] = 0
                    cnt += abs(cur-arr[i][0]) + 1
                    break
                else :
                    cur += 1

    if cnt < min_cnt :
        min_cnt = cnt
    cnt = 0


    print(arr)
